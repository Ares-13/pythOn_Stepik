a = int(input())
b = int(input())
c = input()

if c == "*":
    print(a * b)
elif c == "/":
    if a == 0 or b == 0:
        print("На ноль делить нельзя!")
    else:
        print(a / b)
elif c == "-":
    print(a - b)
elif c == "+":
    print(a + b)
