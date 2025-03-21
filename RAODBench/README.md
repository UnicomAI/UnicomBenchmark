# RAOD: A Benchmark for Road Abandoned Object Detection from Video Surveillance

## Introduction
We introduce a large-scale Road Abandoned Object Detection (RAOD) benchmark derived from video surveillance, addressing the lack of abundant datasets in current research. This benchmark specifically targets highway scenarios, which have unique challenges not adequately covered by existing autonomous driving datasets due to differences in camera perspective and scope.

We have collected a substantial amount of real-world video clips containing various potential abandoned object categories on highways from our commercial Intelligent Transportation Systems (ITS). The resulting dataset comprises 557 video sequences and 18,953 images, all with pixel-level manual annotations. This extensive dataset provides a rich resource for training and evaluating road abandoned object detection models.

To demonstrate the effectiveness of different approaches, we conducted comprehensive evaluation experiments using a variety of baseline models from mainstream algorithms on our RAOD dataset. These experiments provide insights into the performance of different methods and serve as a benchmark for future research in this area.

We propose a novel image segmentation framework that incorporates an area-aware attention mechanism. Our experimental results show that this method significantly outperforms the UNet-based model, achieving nearly a 9% improvement in dice score. This advancement represents a step forward in the accuracy and reliability of road abandoned object detection.

## RAOD dataset
The RAOD dataset comprises 557 video sequences and 18,953 images, all with pixel-level manual annotations.

Please download RAOD dataset from the following link:
- [Baidu Yun Pan]( https://pan.baidu.com/s/1MdjOxZ2TQ-5PX_cB6PJQYg): 5tGb
- [Google Drive](https://drive.google.com/file/d/1WsaBYKtHT55_bdx0JW2vohxsXjFYMdh9/view?usp=drive_link)

## Citation
If you use our benchmark or dataset in your research, please cite our paper.
```bash
@ARTICLE{10542978,
  author={Xu, Yajun and Hu, Huan and Zhu, Xiaoya and Nan, Yibing and Wang, Kai and Liu, Zhaoxiang and Lian, Shiguo},
  journal={IEEE Access}, 
  title={RAOD: A Benchmark for Road Abandoned Object Detection From Video Surveillance}, 
  year={2024},
  volume={12},
  number={},
  pages={123985-123994},
  keywords={Roads;Benchmark testing;Image segmentation;Video surveillance;Uncertainty;Object recognition;Training;Intelligent transportation systems;Road abandoned object detection;intelligent transportation system;video surveillance;area-aware attention mechanism},
  doi={10.1109/ACCESS.2024.3407955}
}


```
