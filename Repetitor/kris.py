a = {0: "А", 1: "В", 2: "Е", 3: "Н", 4: "С"}

k = 0
for i in range(len(a)):
    for j in range(len(a)):
        for g in range(len(a)):
            for m in range(len(a)):
                k += 1
                word = a[i] + a[j] + a[g] + a[m]
                if "Е" not in word and "АА" not in word:
                    print(k)  # Выведет 27
                    exit()


s = "3" * 6 + "4" * 75

while ("35" in s) or ("355" in s) or ("3444" in s):
    if "35" in s:
        s = s.replace("35", "4", 1)
    elif "355" in s:
        s = s.replace("355", "4", 1)
    else:
        s = s.replace("3444", "3", 1)

print(s)  # даст '333333'
