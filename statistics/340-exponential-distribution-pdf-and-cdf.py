import numpy as np

def exponential_distribution_np(x, lam):
    if lam <= 0:
        return {
            'pdf': None,
            'cdf': None,
            'mean': None,
            'variance': None
        }
    
    x = np.asarray(x)
    exp_term = np.exp(-lam * x)
    
    # 批量处理x<0的情况
    pdf = np.where(x >= 0, lam * exp_term, 0.0)
    cdf = np.where(x >= 0, 1 - exp_term, 0.0)
    
    return {
        'pdf': np.round(pdf, 4).tolist(),
        'cdf': np.round(cdf, 4).tolist(),
        'mean': round(1 / lam, 4),
        'variance': round(1 / (lam**2), 4)
    }

# 测试题目示例
x = [0, 1, 2]
lam = 1.0
print(exponential_distribution_np(x, lam))