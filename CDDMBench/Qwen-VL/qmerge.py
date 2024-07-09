# Modified from https://gist.githubusercontent.com/ChrisHayduk/1a53463331f52dca205e55982baf9930/raw/438ab25f05a8e1dd3c384b81fad38c6101c98be9/merge_qlora_with_quantized_model.py
import argparse
import torch
import peft
import json
import shutil
from peft.utils import _get_submodules
import os
# import bitsandbytes as bnb
# from bitsandbytes.functional import dequantize_4bit
from peft import PeftModel
from transformers import AutoModelForCausalLM, LlamaForCausalLM, LlamaTokenizer, BitsAndBytesConfig #
import transformers
import gc
import copy

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=str)
    parser.add_argument("--peft", type=str)
    parser.add_argument("--out", type=str)
    parser.add_argument("--push", action="store_true")
    return parser.parse_args()

def dequantize_model(model, tokenizer, to, dtype=torch.bfloat16, device="cuda"):
    """
    'model': the peftmodel you loaded with qlora.
    'tokenizer': the model's corresponding hf's tokenizer.
    'to': directory to save the dequantized model
    'dtype': dtype that the model was trained using
    'device': device to load the model to
    """
    if os.path.exists(to):
        shutil.rmtree(to)
    os.makedirs(to, exist_ok=True)
    cls = bnb.nn.Linear4bit
    with torch.no_grad():
        for name, module in model.named_modules():
            if isinstance(module, cls):
                print(f"Dequantizing `{name}`...")
                quant_state = copy.deepcopy(module.weight.quant_state)
                quant_state[2] = dtype
                weights = dequantize_4bit(module.weight.data, quant_state=quant_state, quant_type="nf4").to(dtype)
                new_module = torch.nn.Linear(module.in_features, module.out_features, bias=None, dtype=dtype)
                new_module.weight = torch.nn.Parameter(weights)
                new_module.to(device=device, dtype=dtype)
                parent, target, target_name = _get_submodules(model, name)
                setattr(parent, target_name, new_module)
        model.is_loaded_in_4bit = False
        print("Saving dequantized model...")
        model.save_pretrained(to)
        tokenizer.save_pretrained(to)
        config_data = json.loads(open(os.path.join(to, 'config.json'), 'r').read())
        config_data.pop("quantization_config", None)
        config_data.pop("pretraining_tp", None)
        with open(os.path.join(to, 'config.json'), 'w') as config:
            config.write(json.dumps(config_data, indent=2))
        return model

def main():
    args = get_args()
    model_path = args.base
    adapter_path = args.peft
    device_map = None
    print(f"Loading base model: {model_path}")
    config = transformers.AutoConfig.from_pretrained(
        model_path,
        cache_dir=None,
        trust_remote_code=True,
    )
    config.use_cache = False

    # Load model and tokenizer
    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_path,
        config=config,
        cache_dir=None,
        device_map=device_map,
        trust_remote_code=True,
        quantization_config=None,
    )
    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_path,
        cache_dir=None,
        model_max_length=2048,
        padding_side="right",
        use_fast=False,
        trust_remote_code=True,
    )
    tokenizer.pad_token_id = tokenizer.eod_id
    model = PeftModel.from_pretrained(model=model, model_id=adapter_path)
    model = model.merge_and_unload()
    model.save_pretrained(args.out)
    tokenizer.save_pretrained(args.out)


if __name__ == "__main__":
    main()
