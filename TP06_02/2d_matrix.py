def copier_m1_m2(matrix1, matrix2):
    for M1_line_nb in range(len(matrix1)):
        for M1_column_nb in range(len(matrix1[0])):
            matrix2[len(matrix1[0]) - 1 - M1_column_nb][len(matrix1) - 1 - M1_line_nb] = matrix1[M1_line_nb][M1_column_nb]

M1 = [[1, 2, 3], [4, 5, 6]]
M2 = [[0]*len(M1) for j in range(len(M1[0]))]

copier_m1_m2(M1, M2)
print(f"{M1=}")
print(f"{M2=}")
