s = input()

lst = sorted(set(list(map(int, s.split()))), reverse=True)

for i in range(len(lst)):
    if i < 4:
        print(lst[i], end=" ")


