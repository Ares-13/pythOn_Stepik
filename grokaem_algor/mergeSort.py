def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    if len(left) > 1:
        left = mergeSort(left)
    if len(right) > 1:
        right = mergeSort(right)

    return merge_lst(left, right)


def merge_lst(a, b):
    c = []
    L = len(a)
    R = len(b)

    i = 0
    j = 0

    while i < L and j < R:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]

    return c


n = list(map(int, input().split()))
print(*mergeSort(n))
