def matrix_transpose(matrix):
    return [list(column) for column in zip(*matrix)]

a = [[1,2,3],[4,5,6]]
print(matrix_transpose(a))