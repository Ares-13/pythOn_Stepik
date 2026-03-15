# def read_matrix(filename):
#     """Чтение матрицы из файла."""
#     with open(filename, "r", encoding="utf-8") as f:
#         n, m = map(int, f.readline().split())
#         matrix = []
#         for _ in range(n):
#             row = list(map(int, f.readline().split()))
#             matrix.append(row)
#     return n, m, matrix


# def spiral_clockwise(matrix, n, m):
#     """Обход матрицы по часовой стрелке (спираль)."""
#     result = []
#     top, bottom, left, right = 0, n - 1, 0, m - 1

#     while top <= bottom and left <= right:
#         # Вправо по верхней строке
#         for j in range(left, right + 1):
#             result.append(matrix[top][j])
#         top += 1

#         # Вниз по правому столбцу
#         for i in range(top, bottom + 1):
#             result.append(matrix[i][right])
#         right -= 1

#         # Влево по нижней строке
#         if top <= bottom:
#             for j in range(right, left - 1, -1):
#                 result.append(matrix[bottom][j])
#             bottom -= 1

#         # Вверх по левому столбцу
#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 result.append(matrix[i][left])
#             left += 1

#     return result


# def find_multiples_of_37(digits):
#     found = []
#     n = len(digits)
#     for i in range(n):
#         for j in range(i+1, n+1):
#             num_str = ''.join(map(str, digits[i:j]))
#             num = int(num_str)
#             if num > 0 and num % 37 == 0:
#                 found.append((num, i, j-1))

#     return found


# def write_result(filename, spiral, found):
#     with open(filename, 'w', encoding="utf-8") as f:
#         f.write(f"Спираль: {" ".join(map(str, spiral))}\n\n")
#         if found:
#             f.write("Да, можно составить число кратное 37:\n")
#             for num, i, j in found:
#                 f.write(f"\t{num} (позиции {i}-{j})\n")
#         else:
#             f.write("Нет, нельзя составить число кратное 37")


# n, m, matrix = read_matrix("Repetitor/in.txt")
# spiral = spiral_clockwise(matrix, n, m)
# found = find_multiples_of_37(spiral)
# write_result("out.txt", spiral, found)

f = open("Repetitor/in.txt")

for s in f:
    a = list(map(int, f.readline().split()))
    print(a)
    break
