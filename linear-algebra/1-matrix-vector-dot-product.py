
def matrix_vector_dot(matrix, vector):
    if len(matrix[0]) != len (vector):
        return -1
    result = []
    for row in matrix:
        dot_product = sum(row[i] * vector [i] for i in range (len(vector)))
        result.append(dot_product)
    return result

if __name__ == "__main__":
    matrix1 = [[1,2],[3,4]]
    vector1 = [5, 6]
    print(matrix_vector_dot(matrix1, vector1)) 