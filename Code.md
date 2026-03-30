本项目案例是基于学习的目的，并没有完全复现出专利中的全部
本专利旨在提供一个合理且有意义的科研研究方向，供广大学者和优秀开发者挖掘与实现

项目目录结构：

<img width="265" height="239" alt="{E81FC6BB-41F4-4FB4-A5DB-24C71D793F92}" src="https://github.com/user-attachments/assets/58ad0c74-f920-4ee7-b283-750bfbb0bdc2" />


📖
整体数据流：
![4_K1ThlTvU6LWcHBlP1-t0l_dVQn0ocarthqXkP10nk772Znh_ok6DNOy0d6cZkBQR1J3Aej9pIU5Bi3g4t4QzA2qI5ysYWDm08yJd8ANX6KS7zRrhztAPsRJIZ_MfIH8pmoBzkeBxhJe-Vq3pSSYSaI99DDr5aA0ETD7bkL8cpo-oFmwNa6z28HwBsRbQh-](https://github.com/user-attachments/assets/016334d0-c51e-425e-a75a-d5d214fc50f9)

每个模态的数据先经过特征提取，生成哈希码。

通过线性投影（即专利中的投影矩阵 T），将高维哈希码映射为低维哈希码。

最后用相似性度量（如汉明距离）计算两个模态哈希码之间的相关性。

图中还出现了 label y_j，说明模型训练时使用了类别标签作为监督信号（对应专利中的哈希中心Cl）。

![i0SLo81ViD9Hil7a86YdB4xJEJzeZ48kz-MNJriFPnwjyByp6C02Y7dl7mVUsHUEmY7nKkDe8HUejpissJFW5pWIxe9cARrE1ffiYdtFpUXiIJRMfZkNQkI25rb85IjNnc4FXWcOC4NuQnPRVYHTVsxeOUYZz5UQO5D2WGjNRYQ](https://github.com/user-attachments/assets/a1f96a8b-e394-40cf-8cc0-4093e09ead16)

特征提取：使用深度学习模型（如图像的 ViT、文本的 GPT-2）提取原始数据的高层语义特征。

哈希生成：将连续特征转换为哈希表示（对应专利中基于 softmax 的哈希学习）。

降维：通过投影矩阵将高维哈希码压缩为低维哈希码。

最终输出：得到可用于检索的紧凑哈希码。

整个流程体现了专利的核心思想：先提取高维语义，再降维压缩，避免直接生成低维哈希带来的信息损失。

![sDHQibvhIOMHv6-z_kdNCE8ikn0Y89Cflbp5mnTynUNmqD8XuTlI9WWu-1oEaLzzCfqCankbJ3yDqB_UbzbPmh5u_f3WDaRdhPfJCyPvkPnYhFgfv_TgU_bABgEr5agzZpTGBUA1DcaZMato6_SAOpJ6y8qGAYnzP6lf5Kk2w7GQo32Lf-T-aQmWTFEm2Imy](https://github.com/user-attachments/assets/e14a788b-deb9-4486-88c2-4b2175cc9855)

这是一张检索阶段的示意图，对应专利中的“哈希检索流程”。

左侧：数据库中的所有图像预先经过哈希映射 ϕ生成哈希码并存储。

右侧：查询图像输入后，经过相同的映射得到哈希码。

通过计算查询哈希码与数据库中所有哈希码的相似度（如汉明距离），快速返回检索结果。

体现了哈希检索的高效性：预存哈希码 + 快速距离计算。


应用场景（RAG）
![IorZC19moIRAlp8iR0loNPeGvlVJ4TPUgH55hsrOUFqA6z_LfgFQBDkF2MK-HPiHl7BM__fQPs5A5X3JVNpY8c0ZhvvR6UshHR2QVn3VyuKHFHHxNFzzRN5Miw04HYll4GXz9wOKu1NpHUAeDy4KDl2Go5T360OEyjnrspcvGD0FnDmUAAHaEw8GN07OmAT7](https://github.com/user-attachments/assets/171c73ae-6736-4bef-8406-ef9ea26e52d4)

清晰地展示了检索流水线：
用户问题输入。

调用嵌入生成服务（即哈希编码服务）将问题转为哈希码。

在向量数据库中检索相关文档（通过哈希码匹配）。

检索到的相关文档与原始问题共同构成上下文。

组装成多模态提示，输入到多模态 LLM 中生成回答。

这里的“向量数据库”可以理解为存储了所有数据的哈希码索引库，对应专利中的“被查询数据库”。



