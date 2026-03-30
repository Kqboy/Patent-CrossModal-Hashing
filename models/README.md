📖TextEncoder（文本编码器）

👉 含义：
输入：一句话（token序列）
输出：512维向量

👉 本质：
把文本变成向量（类似专利里的 z_y）

📖HashModule（🔥核心）

Why 是 bits * 2？
比如：
64bit哈希 → 输出128维
每2个值表示1bit：
[0.2, 0.8] → bit=1
[0.7, 0.3] → bit=0

discretize()
torch.argmax(prob, dim=-1)
把概率变成真正的二值：
[0.2, 0.8] → 1
[0.7, 0.3] → 0

HashModule = “连续特征 → 概率哈希 → 二值哈希”
✔ softmax
✔ argmax
✔ 哈希离散化

📖Projection（长短映射）

self.proj = nn.Linear(high_dim, low_dim)
👉 含义：
输入：64维 hash
输出：16维 hash

👉 本质：
高维 → 低维（压缩）
在降维的同时尽量不损失信息

📖TextEncoder

