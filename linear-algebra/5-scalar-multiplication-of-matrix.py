
def scalar_multiply(matrix, scalar):
    # 双层列表推导式，逐行逐元素完成乘法运算
    return [[num * scalar for num in row] for row in matrix]

matrix = [[1, 2], [3, 4]]
scalar = 2
print(scalar_multiply(matrix, scalar))
# 输出: [[2, 4], [6, 8]]