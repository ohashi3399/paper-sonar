# 🏊swimmer
- 論文のタイトルを入力に、類似した論文を提示するコード

## 対象
- 論文のタイトルとアブストラクトが取得できる会議

> [!NOTE]
> 現在はICLR2025のみ対応しています

## 実装手順
1. タイトルとアブストの先頭500文字とURLを平文で連結
2. [埋め込みモデル](https://huggingface.co/BAAI/bge-m3)でvectorstoreに変換
3. [近似最近傍探索](https://github.com/facebookresearch/faiss)で類似したn件の論文情報を出力


# case study

```
quey: Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models

title: Common Pitfalls of Margin-based Preference Optimization in Language Model Alignment
url: https://iclr.cc//virtual/2025/poster/29259
abstruct: Reinforcement Learning from Human Feedback (RLHF) has become the predominant approach for aligning language models (LMs) to be more helpful and less harmful. At its core, RLHF uses a margin-based loss for preference optimization, which specifies the ideal LM behavior only in terms of the difference between preferred and dispreferred responses. This under-specification of ideal behavior for each response individu
query: Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models
--------------------------------------------------
title: Unintentional Unalignment: Likelihood Displacement in Direct Preference Optimization
url: https://iclr.cc//virtual/2025/poster/27968
abstruct: Direct Preference Optimization (DPO), and its numerous variants, are increasingly used for aligning language models. Although they are designed to teach a model to generate preferred responses more frequently relative to dispreferred responses, prior work has observed that the likelihood of preferred responses often decreases during training. The current work sheds light on the causes and implications of this c
query: Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models
--------------------------------------------------
title: Preference Optimization for Reasoning with Pseudo Feedback
url: https://iclr.cc//virtual/2025/poster/28622
abstruct: Preference optimization techniques, such as Direct Preference Optimization (DPO), are frequently employed to enhance the reasoning capabilities of large language models (LLMs) in domains like mathematical reasoning and coding, typically following supervised fine-tuning. These methods rely on high-quality labels for reasoning tasks to generate preference pairs; however, the availability of reasoning datasets with human-verified labels is
query: Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models
--------------------------------------------------
title: Preference Optimization as Probabilistic Inference
url: https://iclr.cc//virtual/2025/poster/31025
abstruct: Existing preference optimization methods are mainly designed for directly learning from human feedback with the assumption that paired examples (preferred vs. dis-preferred) are available. In contrast, we propose a method that can leverage unpaired preferred or dis-preferred examples by decoupling learning from positive and negative feedback, allowing control over the contribution of each, and works even when only one type of feedback (positive
query: Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models
--------------------------------------------------
title: Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Modelss
url: https://iclr.cc//virtual/2025/poster/30685
abstruct: Multimodal Large Language Models (MLLMs) exhibit promising advancements across various tasks, yet they still encounter significant trustworthiness issues. Prior studies apply Split Conformal Prediction (SCP) in language modeling to construct prediction sets with statistical guarantees. However, these methods typically rely on internal model logits or are restricted to multiple-choice se
query: Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models
--------------------------------------------------
title: Self-Play Preference Optimization for Language Model Alignment
url: https://iclr.cc//virtual/2025/poster/29189
abstruct: Standard reinforcement learning from human feedback (RLHF) approaches relying on parametric models like the Bradley-Terry model fall short in capturing the intransitivity and irrationality in human preferences. Recent advancements suggest that directly working with preference probabilities can yield a more accurate reflection of human preferences, enabling more flexible and accurate language model alignment. In this paper, we propos
query: Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models
--------------------------------------------------
title: TODO: Enhancing LLM Alignment with Ternary Preferences
url: https://iclr.cc//virtual/2025/poster/27951
abstruct: Aligning large language models (LLMs) with human intent is critical for enhancing their performance across a variety of tasks. Standard alignment techniques, such as Direct Preference Optimization (DPO), often rely on the binary Bradley-Terry (BT) model, which can struggle to capture the complexities of human preferences—particularly in the presence of noisy or inconsistent labels and frequent ties. To address these limitations, we introduc
query: Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models
--------------------------------------------------
title: SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection
url: https://iclr.cc//virtual/2025/poster/29422
abstruct: Fine-tuning on task-specific data to boost downstream performance is a crucial step for leveraging Large Language Models (LLMs). However, though fine-tuning enhances the model performance for specialized applications, previous studies have demonstrated that fine-tuning the models on several adversarial samples or even benign data can greatly comprise the model's pre-equipped alignment and safety capabilities. In this work,
query: Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models
--------------------------------------------------
title: Eliminating Position Bias of Language Models: A Mechanistic Approach
url: https://iclr.cc//virtual/2025/poster/28841
abstruct: Position bias has proven to be a prevalent issue of modern language models (LMs), where the models prioritize content based on its position within the given context. This bias often leads to unexpected model failures and hurts performance, robustness, and reliability across various applications. A simple mechanistic analysis attributes the position bias to two components employed in nearly all state-of-the-art LMs: causal atte
query: Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models
--------------------------------------------------
title: SimPER: Simple Preference Fine-Tuning without Hyperparameters by Perplexity Optimization
url: https://iclr.cc//virtual/2025/poster/28626
abstruct: Preference optimization has made significant advances in aligning large language models with preference data. However, existing preference optimization objectives require additional hyperparameters that must be extensively manually adjusted to achieve optimal performance, increasing the complexity and time required for fine-tuning large language models. In this paper, we propose a simplehyperparameter-free 
query: Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models
--------------------------------------------------
```