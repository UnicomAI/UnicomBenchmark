# A Multimodal Benchmark Dataset and Model for Crop Disease Diagnosis

## Introduction
CDDM dataset is the crop disease domain multimodal dataset, a pioneering resource designed to advance the field of agricultural research through the application of multimodal learning techniques. 

We provide the CDDM dataset and our baseline model with Qwen-VL.

Todo list:
- [x] CDDM dataset
- [ ] Qwen-VL baseline weight


## CDDM dataset
### CDDM full images:
- [Google Drive](https://drive.google.com/file/d/1WA1LH1XY77BUEUyE42rVpvWVh8Z3p_hD/view?usp=drive_link)
- [Baidu Yun Pan](https://pan.baidu.com/s/1WxTMJOv5gZWzmmE6otDljA?pwd=iq2x): iq2x

### CDDM QAs:
- [QA_zh](dataset/QA_zh/)
- [QA_en](dataset/QA_en/)

## Train
### To run on a machine with 8 GPUs:
```shell
cd Qwen-VL
sh finetune/finetune_lora_ds.sh
```


