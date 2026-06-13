
import numpy as np

def normal_equation(X, y):
    # 1. 转换为numpy数组，确保y是一维向量（兼容二维输入）
    X_np = np.array(X)
    y_np = np.array(y).ravel()
    
    # 2. 计算正规方程各组件
    X_transpose = X_np.T          # 转置X
    XtX = X_transpose @ X_np      # 计算X^T X
    XtX_inv = np.linalg.inv(XtX)  # 计算逆矩阵
    Xty = X_transpose @ y_np      # 计算X^T y
    
    # 3. 求解θ并四舍五入到4位小数
    theta = XtX_inv @ Xty
    theta_rounded = np.round(theta, 4)
    
    # 4. 转换为列表返回（符合题目输出格式）
    return theta_rounded.tolist()

X = [[1, 5], [1, 10], [1, 15]]
y = [7, 12, 17]
print(normal_equation(X, y))  # 输出: [2.0, 1.0]（模型：y=2+1*x）