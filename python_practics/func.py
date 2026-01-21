def wrap(tp):
    def inner(lst):
        if tp == "list":
            return list(lst)
        else:
            return tuple(lst)
    
    return inner

s1 = input()
s2 = map(int, input().split())
lst = wrap(s1)
print(lst(s2))
