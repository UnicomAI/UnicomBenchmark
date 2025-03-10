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

## Train
### Qwen-VL: To run on a machine with 8 GPUs:
```shell
cd Qwen-VL
sh finetune/finetune_lora_ds.sh
```

## Citation
If you find our dataset or model useful, please cite our work:

```bibtex
@inproceedings{liu2024multimodal,
  title={A Multimodal Benchmark Dataset and Model for Crop Disease Diagnosis},
  author={Liu, Xiang and Liu, Zhaoxiang and Hu, Huan and Chen, Zezhou and Wang, Kohou and Wang, Kai and Lian, Shiguo},
  booktitle={European Conference on Computer Vision},
  pages={157--170},
  year={2024},
  organization={Springer}
}
```
## Paper
For more details, please refer to our paper: [ECCV 2024 Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/11606.pdf)
