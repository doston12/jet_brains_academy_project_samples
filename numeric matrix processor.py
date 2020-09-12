# Solution for stage 3/6 of Numeric matrix processor project
# new comment line

def init_matrix(rows):
    matrix = []

    for i in range(rows):
        temp = list(map(float, input().split(' ')))
        matrix.append(temp)

    return matrix

def print_matrix(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print()
    print()

def add_matricies(matrix1, matrix2, rows, cols):
    res_matrix = []
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(matrix1[i][j] + matrix2[i][j])
        res_matrix.append(temp)
    return res_matrix

def multiply_matrix_by_constant(number, matrix, rows, cols):
    print("The result is")
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] *= number

    return matrix

def multiply_matricies(matrix1, rows1, cols1, matrix2, cols2):
    res_matrix = []
    for i in range(rows1):
        temp = []
        for j in range(cols2):
            x = 0
            for k in range(cols1):
                    x += matrix1[i][k] * matrix2[k][j]
            temp.append(x)
        res_matrix.append(temp)

    return res_matrix

def print_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")


while True:
    print_menu()
    user_option = int(input("Your choice: "))


    if user_option == 1:
        matrix1_rows, matrix1_cols = map(int, input("Enter size of first matrix: ").split(' '))
        print("Enter first matrix:")
        matrix1 = init_matrix(matrix1_rows)

        matrix2_rows, matrix2_cols = map(int, input("Enter size of second matrix: ").split(' '))
        print("Enter second matrix:")
        matrix2 = init_matrix(matrix2_rows)

        res_matrix = add_matricies(matrix1, matrix2, matrix1_rows, matrix1_cols)
        print_matrix(res_matrix, matrix1_rows, matrix1_cols)

    elif user_option == 2:
        matrix1_rows, matrix1_cols = map(int, input("Enter size of second matrix: ").split(' '))
        print("Enter matrix: ")

        matrix1 = init_matrix(matrix1_rows)
        number = int(input("Enter constant: "))

        res_matrix = multiply_matrix_by_constant(number, matrix1, matrix1_rows, matrix1_cols)
        print_matrix(res_matrix, matrix1_rows, matrix1_cols)

    elif user_option == 3:
        matrix1_rows, matrix1_cols = map(int, input("Enter size of first matrix: ").split(' '))
        print("Enter first matrix:")
        matrix1 = init_matrix(matrix1_rows)

        matrix2_rows, matrix2_cols = map(int, input("Enter size of second matrix: ").split(' '))
        print("Enter second matrix:")
        matrix2 = init_matrix(matrix2_rows)

        if matrix1_cols == matrix2_rows:
            matrix = multiply_matricies(matrix1, matrix1_rows, matrix1_cols, matrix2, matrix2_cols)
            print_matrix(matrix, matrix1_rows, matrix2_cols)
        else:
            print("The operation cannot be performed.")
            print()

    elif user_option == 0:
        break

