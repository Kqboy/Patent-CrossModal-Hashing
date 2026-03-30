import torch
import torch.nn.functional as F

def similarity_loss(img_hash, txt_hash):
    return F.mse_loss(img_hash, txt_hash)

def quantization_loss(prob):
    binary = torch.round(prob)
    return F.mse_loss(prob, binary)

def total_loss(img_hash, txt_hash, prob, alpha=0.1):
    return similarity_loss(img_hash, txt_hash) + alpha * quantization_loss(prob)
