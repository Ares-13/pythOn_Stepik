def is_ascending(row, m):
    result = True
    for i in range(m-1):
        if row[i] >= row[i+1]:
            result = False
            break
    
    return result

def mean_sum(row, m, b):
    idx = -1
    for i in range(m):
        if row[i] > b:
            idx = i
            break

    if idx == -1:       #Если нету больше B
        return None, -1
    if idx == 0:        # Если B первый элемент
        return None, 0
    
    s = 0.0
    for j in range(idx):
        s += row[j]
    
    mean = s / idx 

    return mean, idx


def swap_halves(row, m):
    new_row = [0.0] * m
    half = m // 2

    if m % 2 == 0:
        for i in range(half):
            new_row[i] = row[half + 1]
            new_row[half + i] = row[i]
    else:
        for i in range(half):
            new_row[i] = row[half + 1 + i]
            new_row[half + 1 + i] = row[i]
        
        new_row[half] = row[half]

    return new_row
