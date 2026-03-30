# 🔍 Cross-Modal Hashing via Long-Short Mapping

> 📌 本仓库展示了我们专利方法的工程化实现，用于高效的跨模态检索。

---

## 📜 专利说明

本仓库基于以下专利：

**一种基于长短映射的跨模态哈希检索方法**

* 📄 [查看专利 PDF](./docs/一种基于长短映射的跨模态哈希检索方法.pdf)
* 🌐 在线地址：https://kqboy.github.io/一种基于长短映射的跨模态哈希检索方法.pdf

---

## 🧠 概述

跨模态检索的目标是在不同模态之间进行数据搜索（例如，用图像检索文本，或用文本检索图像）。

传统方法通常存在以下问题：

* 存储成本高（连续特征）
* 计算复杂度高
* 低维哈希映射过程中存在信息损失

### 💡 我们的解决方案

我们提出了一种**基于长短映射的跨模态哈希检索框架**，该框架：

* 学习**高维哈希表示**
* 通过投影矩阵将其映射到**低维空间**
* 在保证检索性能的同时实现降维

---

## 🚀 主要贡献

* 🔹 **长短映射机制**

  * 在降低哈希编码维度的同时保持检索精度

* 🔹 **基于 Softmax 的哈希学习**

  * 避免了传统哈希方法（如符号函数）中不可导的问题

* 🔹 **双损失优化**

  * 相似性损失 → 提升检索准确率
  * 量化损失 → 提升离散化质量

* 🔹 **基于 Transformer 的特征提取**

  * 对图像和文本模态进行统一建模

---

## 🏗️ 方法流程

本方法的整体工作流程如下：

```text
图像 / 文本输入
        ↓
Transformer 编码器
        ↓
高维哈希表示
        ↓
投影矩阵（长 → 短映射）
        ↓
低维哈希编码
        ↓
汉明距离检索

---

## ⚙️ Model Architecture

系统包含以下模块：

🖼️ 图像编码器

CNN + Transformer 编码器

📝 文本编码器

字节编码 + Transformer 编码器

🔢 哈希学习模块

多层感知机

基于 Softmax 的二值编码

🔁 投影模块

学习从高维到低维哈希编码的映射

## 📦 Project Structure

```text
.
├── README.md
├── docs/
│   ├── patent.pdf
│
├── demo/
│   ├── inference_demo.py
│
├── models/
│   ├── image_encoder.py
│   ├── text_encoder.py
│   ├── hash_module.py
│   ├── projection.py
│
├── train/
│   ├── train.py
│   ├── loss.py
│
├── results/
│   ├── retrieval_examples.png
│   ├── comparison.md
│
└── requirements.txt
```

---

## ▶️ Demo

运行一个简单的跨模态检索示例：

```bash
python demo/inference_demo.py
```

### Example Tasks

🖼️ 图像 → 检索相关文本

📝 文本 → 检索相关图像

---

## 📊 Retrieval Strategy

将数据库中的所有样本转换为低维哈希编码

将查询样本也转换为哈希编码

使用以下方式计算相似度：

```text
Hamming Distance
```

* Return top-K most similar results

---

## 📉 Loss Function

模型通过以下损失进行优化：

### 1️⃣ Similarity Loss (Ls)

* 保持图像与文本之间的语义相似性

### 2️⃣ Quantization Loss (Lq)

* 减小连续哈希与离散哈希编码之间的误差

### Final Objective:

```text
L = Ls + α * Lq
```

---

## 🧪 Applications

🔍 图像-文本检索

🧠 多模态搜索引擎

📱 推荐系统

🗂️ 大规模多媒体索引

---

## 🛠️ Requirements

```bash
pip install -r requirements.txt
```

---

## 📌 Notes

* This repository provides an **engineering interpretation** of the patented method.
* The implementation is **simplified for demonstration and educational purposes**.
* Full industrial-level deployment may require:

  * Large-scale datasets
  * Distributed training
  * Model optimization

---

## 👨‍💻 Authors

* 刘学亮
* 涂俊锋
* 闫坤祺
* 郝世杰
* 洪日昌
* 汪萌
* 蒋贻顺

---

## 📄 License

This project is for academic and research purposes only.

---

## ⭐ Acknowledgement

If you find this work useful, feel free to ⭐ the repository!
