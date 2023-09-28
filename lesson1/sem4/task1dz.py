# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

matrix = [[1, 2, 3], [4, 5, 6]]


def transpose(matrix):
    transposed = [[0 for i in range(len(matrix))] for j in
                   range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]
    return transposed


print(transpose(matrix))
