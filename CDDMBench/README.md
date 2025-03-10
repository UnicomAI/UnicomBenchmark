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
@InProceedings{10.1007/978-3-031-73016-0_10,
author="Liu, Xiang
and Liu, Zhaoxiang
and Hu, Huan
and Chen, Zezhou
and Wang, Kohou
and Wang, Kai
and Lian, Shiguo",
editor="Leonardis, Ale{\v{s}}
and Ricci, Elisa
and Roth, Stefan
and Russakovsky, Olga
and Sattler, Torsten
and Varol, G{\"u}l",
title="A Multimodal Benchmark Dataset and Model for Crop Disease Diagnosis",
booktitle="Computer Vision -- ECCV 2024",
year="2025",
publisher="Springer Nature Switzerland",
address="Cham",
pages="157--170",
abstract="While conversational generative AI has shown considerable potential in enhancing decision-making for agricultural professionals, its exploration has predominantly been anchored in text-based interactions. The evolution of multimodal conversational AI, leveraging vast amounts of image-text data from diverse sources, marks a significant stride forward. However, the application of such advanced vision-language models in the agricultural domain, particularly for crop disease diagnosis, remains underexplored. In this work, we present the crop disease domain multimodal (CDDM) dataset, a pioneering resource designed to advance the field of agricultural research through the application of multimodal learning techniques. The dataset comprises 137,000 images of various crop diseases, accompanied by 1 million question-answer pairs that span a broad spectrum of agricultural knowledge, from disease identification to management practices. By integrating visual and textual data, CDDM facilitates the development of sophisticated question-answering systems capable of providing precise, useful advice to farmers and agricultural professionals. We demonstrate the utility of the dataset by finetuning state-of-the-art multimodal models, showcasing significant improvements in crop disease diagnosis. Specifically, we employed a novel finetuning strategy that utilizes low-rank adaptation (LoRA) to finetune the visual encoder, adapter and language model simultaneously. Our contributions include not only the dataset but also a finetuning strategy and a benchmark to stimulate further research in agricultural technology, aiming to bridge the gap between advanced AI techniques and practical agricultural applications. The dataset is available at https://github.com/UnicomAI/UnicomBenchmark/tree/main/CDDMBench.",
isbn="978-3-031-73016-0"
}
```
## Paper
For more details, please refer to our paper: [ECCV 2024 Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/11606.pdf)
