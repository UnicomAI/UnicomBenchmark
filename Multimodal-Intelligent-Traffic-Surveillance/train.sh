#
nproc_per_node=8

CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
NPROC_PER_NODE=$nproc_per_node \
swift sft \
    --model models/Qwen/Qwen2.5-VL-7B-Instruct \
    --train_type lora \
    --dataset swift_data/v1.0_train_all.jsonl \
    --val_dataset swift_data/v1.0_test.jsonl \
    --torch_dtype bfloat16 \
    --num_train_epochs 1 \
    --per_device_train_batch_size 2 \
    --lora_rank 8 \
    --lora_alpha 32 \
    --learning_rate 1e-4 \
    --gradient_accumulation_steps $(expr 16 / $nproc_per_node) \
    --eval_steps 50000 \
    --save_steps 1000 \
    --save_total_limit 3 \
    --logging_steps 5 \
    --gradient_checkpointing_kwargs '{"use_reentrant": false}' \
    --output_dir output \
    --attn_impl flash_attn \
    --max_pixels 2073600

