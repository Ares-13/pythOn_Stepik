def isPalindrome(x: int) -> bool:
    '''Решение без преобраз. в строку'''
    # if x < 0:
    #     return False

    # original = x
    # reversed_x = 0

    # while x > 0:
    #     reversed_x = reversed_x * 10 + x % 10
    #     x //=10

    # return original == reversed_x

    return str(x) == str(x)[::-1]


x = int(input())
print(isPalindrome(x))
