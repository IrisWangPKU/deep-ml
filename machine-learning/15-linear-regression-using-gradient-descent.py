
import numpy as np

def linear_regression_gradient_descent(X, y, alpha, iterations):
    # 获取样本数m和特征数n（包括截距项）
    m, n = X.shape
    
    # 初始化所有权重为0（符合题目要求）
    theta = np.zeros(n)
    
    # 批量梯度下降迭代过程
    for _ in range(iterations):
        # 1. 计算预测值 h_θ(x) = Xθ
        y_hat = X @ theta  # 等价于 np.dot(X, theta)
        
        # 2. 计算预测误差 e = y_hat - y
        error = y_hat - y
        
        # 3. 计算MSE损失的梯度 ∇L = (1/m) X^T e
        gradient = (1 / m) * X.T @ error
        
        # 4. 沿负梯度方向更新权重
        theta -= alpha * gradient
    
    # 返回最终学习到的权重
    return theta

# 测试题目中的示例
if __name__ == "__main__":
    X = np.array([[1, 1], [1, 2], [1, 3]])
    y = np.array([3, 5, 7])
    alpha = 0.1
    iterations = 1000
    
    theta = linear_regression_gradient_descent(X, y, alpha, iterations)
    print("Learned coefficients:", theta)
    # 输出: Learned coefficients: [1. 2.]