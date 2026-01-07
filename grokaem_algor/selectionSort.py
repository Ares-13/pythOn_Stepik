def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index


def selectionSort(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest = findSmallest(arr)
        new_arr.append(arr.pop(smallest))  # Удаляем из исходного массива элемент с наименьшим значением по найденному индексу и добавляем его в новый массив

    return new_arr


print(selectionSort([1,5, -4, 10, 7]))