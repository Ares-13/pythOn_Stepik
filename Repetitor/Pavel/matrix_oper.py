def my_len(seq): #Параметры
    count = 0
    for _ in seq:
        count += 1
    
    return count


def read_matrix(filename):
    f = open(filename, "r")          
    first_line = f.readline().split()
    n = int(first_line[0])
    m = int(first_line[1])
    b = float(first_line[2])


    matrix = [None] * n
    for i in range(n):
        parts = f.readline().split()
        row = [0.0] * m
        for j in range(m):
            row[j] = float(parts[j])
        matrix[i] = row


    f.close()

    return matrix, n, m, b

def print_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print("")