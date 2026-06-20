
import numpy as np

def gaussian_mle(data: np.ndarray) -> tuple[float, float]:
    # MLE 均值 = 样本均值
    mu_mle = np.mean(data)
    # MLE 方差 = 有偏样本方差（分母为n，ddof=0）
    var_mle = np.var(data, ddof=0)
    return (mu_mle, var_mle)

# 测试例题
data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print(gaussian_mle(data))  # 输出 (3.0, 2.0)