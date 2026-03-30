5️⃣ Loss（损失函数）

L = similarity_loss + α * quantization_loss


🔹 similarity_loss
MSE(img_hash, txt_hash)

👉 作用：让“同一语义的图和文本”更接近

🔹 quantization_loss

MSE(prob, round(prob))

👉 作用：让概率更接近0/1（方便离散）


| Loss         | 作用    |
| ------------ | ----- |
| similarity   | 对齐语义  |
| quantization | 强化二值化 |




Train.py

训练过程：

img_feat = img_enc(img)
txt_feat = txt_enc(txt)

👉 得到两个模态的特征

img_prob = hash_module(img_feat)
txt_prob = hash_module(txt_feat)

👉 转成“概率哈希”

img_hash = discretize()
txt_hash = discretize()

👉 转成“二进制”

img_low = proj(img_hash)
txt_low = proj(txt_hash)

👉 降维（长短映射）

loss.backward()

👉 学习：
  encoder
  hash
  projection
