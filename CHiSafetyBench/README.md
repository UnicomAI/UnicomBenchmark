# CHiSafetyBench: A Chinese Hierarchical Safety Benchmark for Large Language Models



## Introduction
CHiSafetyBench is a dedicated safety benchmark for evaluating LLMs’ capabilities in identifying risky content and refusing answering risky questions in Chinese contexts. CHiSafetyBench incorporates a dataset that covers a hierarchical Chinese safety taxonomy consisting of 5 risk areas and 31 categories. This dataset comprises two types of tasks: multiple-choice questions and question-answering, evaluating LLMs from the perspectives of risk content identification and the ability to refuse answering risky questions respectively.

* We collect and open-source the first Chinese hierarchical safety assessment dataset, which comprises two types of task data: multiple-choice questions(MCQ) and question-answering(QA). Specifically, The MCQ data primarily focuses on risk content identification, while the QA data consists of risky questions that must be refused. The combination of two task data enhances the diversity of safety verification, facilitating a comprehensive safety evaluation of LLMs.

* We propose an automatic evaluation method based on LLMs, facilitating cost-effective and efficient testing of model safety detection and defense capabilities, significantly reducing the burden of human evaluation.

* We conduct a comprehensive safety evaluation of 12 SOTA Chinese LLMs. By comparing the performance of different models, we provide LLM developers with a safety reference for model usage.

![figure1](./images/figure1.png)

## Evaluation

- **Risk Content Identification**

  The evaluation is conducted directly based on the correctness of the large model's selections. The evaluation metric is ACC (Accuracy).

- **Refusal to Answer**

  The questions and their corresponding large model's response are fed into the Qwen-72B model for automatic assessment. The evaluation metrics are:

  - Rejection Rate (RR-1): Measures the percentage of questions where the model refuses to answer.
  - Responsible Response Rate (RR-2): Evaluates the percentage of answers that are deemed responsible and appropriate.
  - Harm Rate (HR): Calculates the percentage of responses that are considered harmful or inappropriate.

- 

  ![figure2](./images/figure2.png)



## Results

- Risk Content Identification

  ![figure3](./images/figure3.png)

- Refuse to Answer

  ![figure4](./images/figure4.png)

## Citation



```
@misc{zhang2024chisafetybench,
      title={CHiSafetyBench: A Chinese Hierarchical Safety Benchmark for Large Language Models}, 
      author={Wenjing Zhang and Xuejiao Lei and Zhaoxiang Liu and Meijuan An and Bikun Yang and KaiKai Zhao and Kai Wang and Shiguo Lian},
      year={2024},
      eprint={2406.10311},
      archivePrefix={arXiv}
}
```

