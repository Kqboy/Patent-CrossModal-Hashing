import torch
import torch.nn as nn
import torch.nn.functional as F

class HashModule(nn.Module):
    def __init__(self, input_dim=512, hash_bits=64):
        super().__init__()
        self.hash_bits = hash_bits
        self.fc = nn.Linear(input_dim, hash_bits * 2)

    def forward(self, x):
        x = self.fc(x)  # (batch, 2*bits)
        x = x.view(-1, self.hash_bits, 2)

        prob = F.softmax(x, dim=-1)  # 每bit的概率
        return prob

    def discretize(self, prob):
        return torch.argmax(prob, dim=-1).float()
