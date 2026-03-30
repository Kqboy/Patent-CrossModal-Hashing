import torch
from image_encoder import ImageEncoder
from text_encoder import TextEncoder
from hash_module import HashModule
from projection import Projection
from loss import total_loss

def train():
    device = "cpu"

    img_enc = ImageEncoder().to(device)
    txt_enc = TextEncoder().to(device)
    hash_module = HashModule().to(device)
    proj = Projection().to(device)

    optimizer = torch.optim.Adam(
        list(img_enc.parameters()) +
        list(txt_enc.parameters()) +
        list(hash_module.parameters()) +
        list(proj.parameters()),
        lr=1e-3
    )

    for epoch in range(5):
        img = torch.randn(8, 3, 32, 32)
        txt = torch.randint(0, 1000, (8, 10))

        img_feat = img_enc(img)
        txt_feat = txt_enc(txt)

        img_prob = hash_module(img_feat)
        txt_prob = hash_module(txt_feat)

        img_hash = hash_module.discretize(img_prob)
        txt_hash = hash_module.discretize(txt_prob)

        img_low = proj(img_hash)
        txt_low = proj(txt_hash)

        loss = total_loss(img_low, txt_low, img_prob)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

if __name__ == "__main__":
    train()
