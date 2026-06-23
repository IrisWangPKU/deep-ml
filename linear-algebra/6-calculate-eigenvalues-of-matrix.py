
def calculate_eigenvalues(matrix):
    # 提取2x2矩阵的四个元素
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    
    # 计算矩阵的迹和行列式
    trace = a + d
    det = a * d - b * c
    
    # 计算判别式的平方根
    discriminant = trace ** 2 - 4 * det
    sqrt_disc = discriminant ** 0.5
    
    # 代入求根公式得到两个特征值
    lambda1 = (trace + sqrt_disc) / 2
    lambda2 = (trace - sqrt_disc) / 2
    
    # 按从高到低降序排序
    eigenvalues = [lambda1, lambda2]
    eigenvalues.sort(reverse=True)
    
    return eigenvalues