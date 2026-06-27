def determinant(matrix):
    n = len(matrix)
    # 对应：拆到2阶就停，直接算（递归出口）
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det_result = 0
    # 对应：沿着第一行，逐个元素算贡献
    for j in range(n):
        # 1. 生成余子矩阵：删掉第0行、第j列
        minor_matrix = []
        for i in range(1, n):  # 跳过第0行，从第1行开始取
            # 删掉第j列：左边取到j，右边从j+1开始，拼起来
            new_row = matrix[i][:j] + matrix[i][j+1:]
            minor_matrix.append(new_row)
        
        # 2. 算符号：棋盘格，第0行第j列，符号是 (-1)^j
        sign = (-1) ** j
        
        # 3. 递归算小矩阵的行列式，乘起来累加
        det_result += matrix[0][j] * sign * determinant(minor_matrix)
    
    return det_result

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(determinant(a))  # 输出：0