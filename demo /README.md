1️⃣ 建数据库（image）
database = torch.randn(10, 3, 32, 32)

👉 模拟10张图片

db_low = proj(hash(discretize(img)))

👉 每张图 → 一个 低维hash码

2️⃣ 查询（text）
query = torch.randint(...)

👉 输入一句话

q_low = proj(hash(...))

👉 得到查询hash

3️⃣ 核心：计算距离
(a != b).sum()

👉 这就是：

汉明距离（Hamming Distance）

汉明距离距离：

A = 101010
B = 100110

差异位 = 2


结果分析：

<img width="447" height="146" alt="{1FBD03C2-ACEF-487A-97C8-BE9148A0EF97}" src="https://github.com/user-attachments/assets/227b3575-8839-4d90-9528-cda7b2e02ca8" />

在数据库的10张图片中
第 9、0、2 张图片最像这个文本


