# 🔍 Cross-Modal Hashing via Long-Short Mapping

> 📌 An engineering-oriented demonstration of our patented method for efficient cross-modal retrieval.

---

## 📜 Patent

This repository is based on our patent:

**一种基于长短映射的跨模态哈希检索方法**

* 📄 [View Patent PDF](./docs/一种基于长短映射的跨模态哈希检索方法.pdf)
* 🌐 Online version: https://kqboy.github.io/一种基于长短映射的跨模态哈希检索方法.pdf

---

## 🧠 Overview

Cross-modal retrieval aims to search data across different modalities (e.g., retrieving images using text or vice versa).

Traditional methods often suffer from:

* High storage cost (continuous features)
* High computational complexity
* Information loss in low-dimensional hashing

### 💡 Our Solution

We propose a **Long-Short Mapping based Cross-Modal Hashing Framework**, which:

* Learns **high-dimensional hash representations**
* Projects them into **low-dimensional space**
* Preserves retrieval performance via a learned projection matrix

---

## 🚀 Key Contributions

* 🔹 **Long-Short Mapping Mechanism**

  * Reduces hash dimension while maintaining accuracy

* 🔹 **Softmax-based Hash Learning**

  * Avoids non-differentiability issues of traditional hashing (e.g., sign function)

* 🔹 **Dual-Loss Optimization**

  * Similarity Loss → improves retrieval accuracy
  * Quantization Loss → improves discretization quality

* 🔹 **Transformer-based Feature Extraction**

  * Unified modeling for image and text modalities

---

## 🏗️ Method Pipeline

The overall workflow of the proposed method:

```text
Image/Text Input
        ↓
Transformer Encoder
        ↓
High-Dimensional Hash Representation
        ↓
Projection Matrix (Long → Short Mapping)
        ↓
Low-Dimensional Hash Code
        ↓
Hamming Distance Retrieval
```

---

## ⚙️ Model Architecture

The system consists of:

* 🖼️ **Image Encoder**

  * CNN + Transformer Encoder

* 📝 **Text Encoder**

  * Byte Encoding + Transformer Encoder

* 🔢 **Hash Learning Module**

  * Multi-Layer Perceptron (MLP)
  * Softmax-based binary encoding

* 🔁 **Projection Module**

  * Learns mapping from high-dim to low-dim hash codes

---

## 📦 Project Structure

```text
.
├── README.md
├── docs/
│   ├── patent.pdf
│
├── demo/
│   ├── inference_demo.py
│   ├── sample_data/
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

Run a simple cross-modal retrieval demo:

```bash
python demo/inference_demo.py
```

### Example Tasks

* 🖼️ Image → Retrieve relevant text
* 📝 Text → Retrieve relevant images

---

## 📊 Retrieval Strategy

* Convert all database samples into **low-dimensional hash codes**
* Convert query into hash code
* Compute similarity using:

```text
Hamming Distance
```

* Return top-K most similar results

---

## 📉 Loss Function

The model is optimized using:

### 1️⃣ Similarity Loss (Ls)

* Preserves semantic similarity between image and text

### 2️⃣ Quantization Loss (Lq)

* Reduces error between continuous and discrete hash codes

### Final Objective:

```text
L = Ls + α * Lq
```

---

## 🧪 Applications

* 🔍 Image-Text Retrieval
* 🧠 Multimodal Search Engines
* 📱 Recommendation Systems
* 🗂️ Large-scale Multimedia Indexing

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

* 闫坤祺
* 刘学亮
* 涂俊锋
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
