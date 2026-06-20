import numpy as np

def law_of_large_numbers(n_samples, population_mean, population_std):
    # 生成 n_samples 个服从正态分布的随机样本
    # loc: 分布的总体均值
    # scale: 分布的总体标准差
    # size: 生成的样本数量
    samples = np.random.normal(
        loc=population_mean,
        scale=population_std,
        size=n_samples
    )
    # 计算样本均值并返回
    sample_mean = np.mean(samples)
    return sample_mean

# 测试题目示例
result = law_of_large_numbers(n_samples=1000, population_mean=0.0, population_std=1.0)
print(round(result, 4))