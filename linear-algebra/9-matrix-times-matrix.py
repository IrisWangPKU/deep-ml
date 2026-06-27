
import numpy as np

def matrix_multiply_np(A, B):
    # 1. 将Python嵌套列表转为NumPy数组
    A_np = np.array(A, dtype=float)
    B_np = np.array(B, dtype=float)
    
    # 2. 直接获取矩阵维度（行数, 列数）
    rows_A, cols_A = A_np.shape
    rows_B, cols_B = B_np.shape
    
    # 3. 维度校验：A的列数必须等于B的行数，不匹配返回-1
    if cols_A != rows_B:
        return -1
    
    # 4. 执行矩阵乘法
    result = A_np @ B_np
    
    # 5. 转回Python嵌套列表，和题目输出格式保持一致
    return result.tolist()
# 测试例1：维度匹配
A = [[1,2],[2,4]]
B = [[2,1],[3,4]]
print(matrix_multiply_np(A, B))
# 输出: [[8.0, 9.0], [16.0, 18.0]]

# 测试例2：维度不匹配
A2 = [[1,2], [2,4]]
B2 = [[2,1], [3,4], [4,5]]
print(matrix_multiply_np(A2, B2))
# 输出: -1