
def calculate_matrix_mean(matrix, mode):
    if mode == 'row':
        return [sum(row) / len(row) for row in matrix]
    elif mode == 'column':
        return [sum(col) / len(col) for col in zip(*matrix)]
    return []

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(calculate_matrix_mean(matrix, 'column'))  # 输出: [4.0, 5.0, 6.0]
print(calculate_matrix_mean(matrix, 'row'))     # 输出: [2.0, 5.0, 8.0]