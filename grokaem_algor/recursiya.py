def fact(n):
    if n == 0 or n == 1:  # Базовый случай
        return 1
    else:
        return n + fact(n - 1)  # Рекурсивный случай

print(fact(3))


def sum(arr):
    if len(arr) == 0: # Базовый случай
        return 0
    else:
        return arr[0] + sum(arr[1:]) # Рекурсивный случай

print(sum([3, 6, 2]))


def count_el(arr):
    if len(arr) == 0:  # Базовый случай
        return 0
    else:
        return 1 + count_el(arr[1:]) # Рекурсивный случай

print(count_el([3, 6, 2]))


def find_max(arr):
    # Базовый случай: если в списке один элемент
    if len(arr) == 1:
        return arr[0]

    # Рекурсивный случай: сравниваем первый элемент с максимумом остальных
    max_el = find_max(arr[1:])

    if arr[0] > max_el:
        return arr[0]
    else:
        return max_el

print(find_max([3, 9, 2]))


def fib_rec(N, f=[1, 1]):
    # Когда список достиг нужной длины, возвращаем первые N элементов
    if len(f) >= N:
        return f[:N]

    # Рекурсивный случай:
    f.append(f[-1] + f[-2])

    return fib_rec(N, f)


N = int(input())
print(*fib_rec(N))
