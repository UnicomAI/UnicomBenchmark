# A Multimodal Benchmark Dataset and Model for Crop Disease Diagnosis

## Introduction
CDDM dataset is the crop disease domain multimodal dataset, a pioneering resource designed to advance the field of agricultural research through the application of multimodal learning techniques. 


## CDDM dataset
The CDDM dataset includes images and conversation data. 
### CDDM images:
Please download CDDM images from the following link and extract it to the /dataset/ directory.
- [Google Drive](https://drive.google.com/file/d/1kfB3zkittoef4BasOhwvAb8Cb66EPXst/view?usp=sharing)
- [Baidu Yun Pan](https://pan.baidu.com/s/1CgmO2MyEKV6EE42eNS0sIw?pwd=ip1r): ip1r


### CDDM conversation:
We offer the conversation data in two formats suitable for training Qwen-VL and LLaVA models. The data covers crop disease diagnosis and knowledge.

Please extract the conversation data to the /dataset/VQA/ directory. 
- [Qwen-VL training data](dataset/VQA/Crop_Disease_train_qwenvl.zip)
- [LLaVA training data](dataset/VQA/Crop_Disease_train_llava.zip)
- [Test data](dataset/VQA/test_dataset.zip)

## Train
### Qwen-VL: To run on a machine with 8 GPUs:
```shell
cd Qwen-VL
sh finetune/finetune_lora_ds.sh
```
## Test
### Measure the accuracy of disease diagnosis
Generate Diagnosis_output.json by performing inference on the test data with the model. Afterward, execute the following code.
```shell
cd script
python disease_diagnosis_accuracy.py
```

## Citation
If you find our dataset or model useful, please cite our work:

```bibtex
@InProceedings{10.1007/978-3-031-73016-0_10,
author="Xiang, Liu
and Zhaoxiang, Liu
and Huan, Hu
and Zezhou, Chen
and Kohou, Wang
and Kai, Wang
and Shiguo, Lian",
title="A Multimodal Benchmark Dataset and Model for Crop Disease Diagnosis",
booktitle="Computer Vision -- ECCV 2024",
year="2025",
publisher="Springer Nature Switzerland",
address="Cham",
pages="157--170",
isbn="978-3-031-73016-0"
}
```
## Paper
For more details, please refer to our paper: [ECCV 2024 Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/11606.pdf)  , [arxiv](https://arxiv.org/abs/2503.06973)
