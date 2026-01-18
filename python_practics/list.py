# треугольник Паскаля

# N = 5
# P = []

# for i in range(N):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j != i:
#             row[j] = P[i-1][j-1] + P[i-1][j]

#     P.append(row)

# for r in P:
#     print(" " * (N - len(r)), end="")
#     # если r = [1, 2, 3], то print(*r) эквивалентно print(1, 2, 3),
#     # и на экране появится строка 1 2 3
#     print(*r, sep=" ")

# I love Python

# Сложение матриц
# a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
# b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
# c = []

# for i, row in enumerate(a):
#     r = []
#     for j, x in enumerate(row):
#         r.append(x + b[i][j])

#     c.append(r)

# print(c)


# Транспонирование матрицы
# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# for i in range(len(A)):
#     for j in range(i + 1, len(A)):
#         A[i][j], A[j][i] = A[j][i], A[i][j]

# for r in A:
#     for x in r:
#         print(x, end="\t")
#     print()


# r = []
# for i in range(1):
#     for j in range(4):
#         r.append(1)
#     r[-1] = 5
# print(*r)


