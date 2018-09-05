import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6]])


def sumRow(matrix, row):
    print(sum(matrix[row]))


def sumColumn(matrix, column):
    total = []
    for i in range(0, len(matrix)):
        total.append(matrix[i][column])
    print(sum(total))


sumRow(matrix, 0)
sumColumn(matrix, 2)
