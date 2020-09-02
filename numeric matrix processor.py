# Solution for stage 1/6 of Numeric matrix processor project

def init_matrix(rows):
    matrix = []

    for i in range(rows):
        temp = list(map(int, input().split(' ')))
        matrix.append(temp)

    return matrix

def print_matrix(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print()

def add_matricies(matrix1, matrix2, rows, cols):
    res_matrix = []
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(matrix1[i][j] + matrix2[i][j])
        res_matrix.append(temp)
    return res_matrix


matrix1_rows, matrix1_cols = map(int, input().split(' '))
matrix1 = init_matrix(matrix1_rows)

matrix2_rows, matrix2_cols = map(int, input().split(' '))
matrix2 = init_matrix(matrix2_rows)


if matrix1_rows == matrix2_rows and matrix1_cols == matrix2_cols:
    res_matrix = add_matricies(matrix1, matrix2, matrix1_rows, matrix1_cols)
    print_matrix(res_matrix, matrix1_rows, matrix1_cols)

else:
    print("ERROR")