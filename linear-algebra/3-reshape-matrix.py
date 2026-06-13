def matrix_reshape(matrix, new_shape):
    if not matrix:
        return []
    
    old_row = len(matrix)
    old_col = len(matrix[0])
    total = old_row * old_col

    new_row, new_col = new_shape

    if total != new_row * new_col:
        return []
    
    flattened = []
    for row in matrix:
        for num in row:
            flattened.append(num)
    
    reshaped = []
    for i in range(new_row):
        start = i * new_col
        end = start + new_col
        new_row_data = flattened[start:end]
        reshaped.append(new_row_data)

    return reshaped


print("测试1 2x4 -> 4x2")
a = [[1, 2, 3, 4], [5, 6, 7, 8]]
new_shape = (4, 2)
print("输入矩阵:", a)
print("目标形状:", new_shape)
print("输出结果:", matrix_reshape(a, new_shape))
print()