
from scipy.stats import beta

def beta_distribution_stats_scipy(x, alpha, beta_param):
    dist = beta(alpha, beta_param)
    return {
        'pdf': round(dist.pdf(x), 4),
        'mean': round(dist.mean(), 4),
        'variance': round(dist.var(), 4)
    }

# 测试题目示例
print(beta_distribution_stats_scipy(0.3, 2, 5))