def quickSort(arr):
    # Базовый случай: массивы с 0 и 1 элементом уже "отсортированы"
    if len(arr) < 2:
        return arr
    # Рекурсивный случай
    else:
        pivot = arr[0] # Опорный элемент
        less = [i for i in arr[1:] if i < pivot]  # Меньше опорного элемента
        greater = [i for i in arr[1:] if i > pivot]  # Больше опорного элемента

        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([-2, 3, 0, 10, 7]))
