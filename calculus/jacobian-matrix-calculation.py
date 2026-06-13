import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
    """
    Compute the Jacobian matrix using numerical differentiation.
    
    Args:
        f: Function that takes a list and returns a list
        x: Point at which to evaluate the Jacobian
        h: Step size for finite differences
    
    Returns:
        Jacobian matrix as list of lists
    """
    # 1. 确定输入维度 n 和输出维度 m
    n = len(x)
    m = len(f(x))
    
    # 2. 初始化 m x n 的 Jacobian 矩阵（全0）
    jacobian = np.zeros((m, n))
    
    # 3. 遍历每一个输入变量 x_j（对应矩阵的列）
    for j in range(n):
        # 构造单位向量 e_j：只有第 j 位是 1，其余是 0
        e_j = np.zeros(n)
        e_j[j] = 1.0
        
        # 计算 x + h*e_j 和 x - h*e_j
        x_plus = np.array(x) + h * e_j
        x_minus = np.array(x) - h * e_j
        
        # 计算 f(x+h*e_j) 和 f(x-h*e_j)
        f_plus = np.array(f(x_plus.tolist()))
        f_minus = np.array(f(x_minus.tolist()))
        
        # 4. 用中心差分法计算第 j 列的所有偏导数
        jacobian[:, j] = (f_plus - f_minus) / (2 * h)
    
    # 5. 转成 list of lists 返回
    return jacobian.tolist()


# ===================== 测试代码（题目例子） =====================
if __name__ == "__main__":
    # 定义题目中的向量值函数 f(x, y) = [x^2, xy, y^2]
    def test_f(x):
        return [x[0]**2, x[0] * x[1], x[1]**2]
    
    # 题目输入点 x = [2, 3]
    x_point = [2.0, 3.0]
    
    # 计算 Jacobian 矩阵
    J = jacobian_matrix(test_f, x_point)
    
    # 打印结果
    print("计算得到的 Jacobian 矩阵：")
    for row in J:
        print(row)