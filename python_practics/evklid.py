def gcd(a, b):\
    #а должно быть больше b
    if a < b:
        a, b = b, a
        
    while b != 0:
        a, b = b, a % b
    return a


def test_gcd(func):
    #--- тест
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print(True)
    else:
        print(False)

test_gcd(gcd)