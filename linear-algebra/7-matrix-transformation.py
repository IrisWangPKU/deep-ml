
import numpy as np

def matrix_transform(A, T, S):
    # 转换为浮点数组，保证计算精度
    A_np = np.array(A, dtype=np.float64)
    T_np = np.array(T, dtype=np.float64)
    S_np = np.array(S, dtype=np.float64)
    
    # 1. 校验T、S为方阵
    if T_np.shape[0] != T_np.shape[1] or S_np.shape[0] != S_np.shape[1]:
        return -1
    
    # 2. 校验矩阵维度匹配
    if T_np.shape[0] != A_np.shape[0] or S_np.shape[0] != A_np.shape[1]:
        return -1
    
    # 3. 校验可逆性：行列式非零（浮点数容差避免精度误差）
    epsilon = 1e-10
    det_T = np.linalg.det(T_np)
    det_S = np.linalg.det(S_np)
    if abs(det_T) < epsilon or abs(det_S) < epsilon:
        return -1
    
    # 4. 计算T的逆矩阵并执行变换
    T_inv = np.linalg.inv(T_np)
    result = T_inv @ A_np @ S_np
    
    # 转换为嵌套列表返回，与输入格式一致
    return result.tolist()

# 测试示例
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    T = [[2, 0], [0, 2]]
    S = [[1, 1], [0, 1]]
    print(matrix_transform(A, T, S))
    # 输出: [[0.5, 1.5], [1.5, 3.5]]