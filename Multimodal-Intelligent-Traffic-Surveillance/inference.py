from PIL import Image
import requests
import torch
from torchvision import io
from typing import Dict
from transformers import Qwen2_5_VLForConditionalGeneration, AutoTokenizer, AutoProcessor


class Qwen2_5VL:
    def __init__(self,model_name, device_map, dtype="auto"):
        self.model_name = model_name
        self.device_map = device_map
        self.max_new_tokens = 512

        self.model = Qwen2_5_VLForConditionalGeneration.from_pretrained(model_name,torch_dtype=dtype, device_map=device_map)
        self.processor = AutoProcessor.from_pretrained(model_name)
    def get_dtype(self):
        first_param = next(self.model.parameters())
        dtype = first_param.dtype
        print("model para precision:", dtype)
        return dtype
    def inference_image(self, query, image_path):
        image = Image.open(image_path)

        # #40G的A100最大只能支持1920x1080推理（Qwen2-VL-7B-Instruct   FP16）,如果分辨率太高需要进行缩放
        width, height = image.size
        if width > 1920 or height > 1080:
            if (1920/width > 1080/height):
                new_height = 1080
                new_width = int(width * (1080 / height))
            else:
                new_width = 1920
                new_height = int(height * (1920 / width))
            image = image.resize((new_width, new_height))
            print("original image size:({0},{1}), resized image: ({2}, {3})".format(width, height, image.size[0], image.size[1]))


        conversation = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                    },
                    {
                        "type": "text",
                        "text": query
                    }
                ]
            }
        ]
        # Preprocess the inputs
        text_prompt = self.processor.apply_chat_template(conversation, add_generation_prompt=True)
        # Excepted output: '<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|>Describe this image.<|im_end|>\n<|im_start|>assistant\n'
        inputs = self.processor(text=[text_prompt], images=[image], padding=True, return_tensors="pt")
        inputs = inputs.to("cuda")
        # Inference: Generation of the output
        output_ids = self.model.generate(**inputs, max_new_tokens=512)  # output length, 256 -> 512
        generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, output_ids)]
        output_text = self.processor.batch_decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        return output_text

if __name__ == "__main__":
    model_name = "Qwen2.5-VL-3B-Instruct-traffic"
    device_map = "cuda:0"
    dtype = "bfloat16"
    sft_model = Qwen2_5VL(model_name, device_map, dtype)
    query_loc = "localize all vehicles, output bounding bboxes."
    image_path = "test_images/20230227-gaosu-707e1f87-30cc-4050-90ba-af11490063ea_105.jpg"
    sft_model.inference_image(query_loc, image_path)[0]