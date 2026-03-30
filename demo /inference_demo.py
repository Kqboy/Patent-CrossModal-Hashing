import torch
from image_encoder import ImageEncoder
from text_encoder import TextEncoder
from hash_module import HashModule
from projection import Projection

def hamming_distance(a, b):
    return (a != b).sum(dim=1)

def main():
    img_enc = ImageEncoder()
    txt_enc = TextEncoder()
    hash_module = HashModule()
    proj = Projection()

    # 模拟数据库
    database = torch.randn(10, 3, 32, 32)
    db_feat = img_enc(database)
    db_prob = hash_module(db_feat)
    db_hash = hash_module.discretize(db_prob)
    db_low = proj(db_hash)

    # 查询文本
    query = torch.randint(0, 1000, (1, 10))
    q_feat = txt_enc(query)
    q_prob = hash_module(q_feat)
    q_hash = hash_module.discretize(q_prob)
    q_low = proj(q_hash)

    # 计算距离
    distances = hamming_distance(q_low.round(), db_low.round())
    topk = torch.topk(-distances, k=3)

    print("Top-3 matched indices:", topk.indices)

if __name__ == "__main__":
    main()
