
def inverse_2x2(matrix):
    # 1. 校验输入是否为2行的矩阵
    if len(matrix) != 2:
        return None
    # 校验每一行是否都有2个元素
    if len(matrix[0]) != 2 or len(matrix[1]) != 2:
        return None
    
    # 2. 提取矩阵四个元素
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    
    # 3. 计算行列式
    det = a * d - b * c
    
    # 4. 判断可逆性：行列式为0则返回None
    # 工程场景建议用浮点数容差：if abs(det) < 1e-10
    if det == 0:
        return None
    
    # 5. 按公式计算逆矩阵
    inv_det = 1.0 / det
    inverse_matrix = [
        [d * inv_det, -b * inv_det],
        [-c * inv_det, a * inv_det]
    ]
    
    return inverse_matrix

# 测试题目示例
if __name__ == "__main__":
    mat = [[4, 7], [2, 6]]
    print(inverse_2x2(mat))
    # 输出: [[0.6, -0.7], [-0.2, 0.4]]