def calculate_covariance_matrix(data):
    # 步骤1：计算每个特征的均值
    means = [sum(feature) / len(feature) for feature in data]
    
    # 步骤2：获取特征数量n和观测值数量m
    n_features = len(data)
    n_observations = len(data[0])
    
    # 步骤3：初始化n×n的协方差矩阵
    cov_matrix = [[0.0 for _ in range(n_features)] for _ in range(n_features)]
    
    # 步骤4：计算每对特征的协方差
    for i in range(n_features):
        for j in range(n_features):
            covariance_sum = 0.0
            # 遍历所有观测值，累加偏差乘积
            for k in range(n_observations):
                deviation_i = data[i][k] - means[i]
                deviation_j = data[j][k] - means[j]
                covariance_sum += deviation_i * deviation_j
            # 样本协方差除以m-1
            cov_matrix[i][j] = covariance_sum / (n_observations - 1)
    
    return cov_matrix

# 测试题目示例（只测试基础版）
data = [[1, 2, 3], [4, 5, 6]]
result = calculate_covariance_matrix(data)
print("协方差矩阵结果：", result)