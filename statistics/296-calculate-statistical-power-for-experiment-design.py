
import math

def normal_cdf(x):
    """标准正态分布累积分布函数(CDF)，用误差函数精确实现"""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def normal_ppf(p):
    """标准正态分布分位数函数(逆CDF)，Abramowitz-Stegun 高精度近似"""
    if p <= 0 or p >= 1:
        raise ValueError("概率值必须在 0 到 1 之间")
    
    # 近似公式系数，工业界通用标准实现
    a1 = 2.50662823884
    a2 = -18.61500062529
    a3 = 41.39119773534
    a4 = -25.44106049637
    b1 = -8.47351093090
    b2 = 23.08336743743
    b3 = -21.06224101826
    b4 = 3.13082909833
    c1 = -2.78718931138
    c2 = -2.29796479134
    c3 = 4.85014127135
    c4 = 2.32121276858
    d1 = 3.54388924762
    d2 = 1.63706781897
    
    q = p - 0.5
    # 中间区域近似
    if abs(q) < 0.42:
        r = q * q
        numerator = (((a4 * r + a3) * r + a2) * r + a1) * q
        denominator = ((((b4 * r + b3) * r + b2) * r + b1) * r + 1)
        return numerator / denominator
    # 尾部区域近似
    else:
        r = p if q < 0 else 1 - p
        r = math.log(-math.log(r))
        x = c1 + r * (c2 + r * (c3 + r * c4))
        x /= 1 + r * (d1 + r * d2)
        return -x if q < 0 else x

def calculate_power(effect_size, sample_size_per_group, alpha=0.05, two_tailed=True):
    # 步骤1：计算非中心参数（两个分布的平移距离）
    ncp = effect_size * math.sqrt(sample_size_per_group / 2)
    
    # 步骤2：计算显著性水平对应的临界值（门槛线）
    if two_tailed:
        z_crit = normal_ppf(1 - alpha / 2)
    else:
        z_crit = normal_ppf(1 - alpha)
    
    # 步骤3：计算统计功效
    if two_tailed:
        # 双侧检验：左右两个拒绝域的概率相加
        power = 1 - normal_cdf(z_crit - ncp) + normal_cdf(-z_crit - ncp)
    else:
        # 单侧检验：仅右侧拒绝域
        power = 1 - normal_cdf(z_crit - ncp)
    
    # 保留四位小数返回
    return round(power, 4)


# 测试题目示例
if __name__ == "__main__":
    result = calculate_power(
        effect_size=0.5,
        sample_size_per_group=64,
        alpha=0.05,
        two_tailed=True
    )
    print("统计功效结果：", result)




