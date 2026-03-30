import torch
import torch.nn as nn

class ImageEncoder(nn.Module):
    def __init__(self, output_dim=512):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Flatten(),
            nn.Linear(3 * 32 * 32, 1024),
            nn.ReLU(),
            nn.Linear(1024, output_dim)
        )

    def forward(self, x):
        return self.encoder(x)
