import torch
import torch.nn as nn

class Projection(nn.Module):
    def __init__(self, high_dim=64, low_dim=16):
        super().__init__()
        self.proj = nn.Linear(high_dim, low_dim, bias=False)

    def forward(self, x):
        return self.proj(x)
