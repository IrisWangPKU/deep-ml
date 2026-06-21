
def calculate_portfolio_variance(cov_matrix, weights):
    # 校验：协方差矩阵非空
    n = len(cov_matrix)
    if n == 0:
        raise ValueError("协方差矩阵不能为空")
    
    # 校验：协方差矩阵是方阵
    for row in cov_matrix:
        if len(row) != n:
            raise ValueError("协方差矩阵必须是方阵")
    
    # 校验：权重长度与矩阵维度匹配
    if len(weights) != n:
        raise ValueError("权重向量长度必须与协方差矩阵维度一致")
    
    # 校验：所有元素为数值类型
    for row in cov_matrix:
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("协方差矩阵元素必须为数字")
    for w in weights:
        if not isinstance(w, (int, float)):
            raise TypeError("权重元素必须为数字")
    
    # 校验：权重之和近似为1（金融场景常规约束）
    weight_sum = sum(weights)
    if abs(weight_sum - 1.0) > 1e-6:
        raise ValueError(f"权重之和必须为1，当前和为 {weight_sum}")
    
    # 双重求和计算组合方差
    variance = 0.0
    for i in range(n):
        for j in range(n):
            variance += weights[i] * weights[j] * cov_matrix[i][j]
    
    return float(variance)


# 测试题目示例
cov_matrix = [[0.1, 0.02], [0.02, 0.15]]
weights = [0.6, 0.4]
print(calculate_portfolio_variance(cov_matrix, weights))  # 输出 0.0696