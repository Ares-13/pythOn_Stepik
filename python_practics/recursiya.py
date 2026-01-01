# считывание числа N
N = int(input())

# здесь продолжайте программу
def get_rec_N(n):
    if n > 0:
        get_rec_N(n - 1)
        print(n)

get_rec_N(N)  # вызов рекурсивной функции
