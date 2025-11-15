# треугольник Паскаля

N = 5
P = []

for i in range(N):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]
    
    P.append(row)

for r in P:
    print(" " * (N - len(r)), end="")
    # если r = [1, 2, 3], то print(*r) эквивалентно print(1, 2, 3), 
    # и на экране появится строка 1 2 3
    print(*r, sep=" ")
