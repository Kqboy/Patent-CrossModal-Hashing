import torch
import torch.nn as nn

class TextEncoder(nn.Module):
    def __init__(self, vocab_size=1000, embed_dim=256, output_dim=512):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.fc = nn.Linear(embed_dim, output_dim)

    def forward(self, x):
        x = self.embedding(x)         # (batch, seq, embed)
        x = x.mean(dim=1)             # 简化：平均池化
        return self.fc(x)
