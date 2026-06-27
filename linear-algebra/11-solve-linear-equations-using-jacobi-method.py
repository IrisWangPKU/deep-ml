
def jacobi(A, b, n):
    # 1. 获取方程组的阶数（变量个数）
    m = len(A)
    # 2. 初始化解向量为全0
    x = [0.0 for _ in range(m)]
    
    # 3. 迭代n次
    for _ in range(n):
        # 关键：新建一个向量存新值，全程用旧x计算
        x_new = [0.0 for _ in range(m)]
        
        for i in range(m):
            # 计算除了对角线项之外的和
            s = 0.0
            for j in range(m):
                if j != i:
                    s += A[i][j] * x[j]
            # 代入公式计算新的x[i]
            x_new[i] = (b[i] - s) / A[i][i]
        
        # 4. 每轮结束保留4位小数，更新x
        x = [round(val, 4) for val in x_new]
    
    return x

# 测试题目里的例子
A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]]
b = [-1, 2, 3]
print(jacobi(A, b, 2))