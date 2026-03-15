def balak_seq(max_len):
    a, b, c = 1, 1, 1

    for _ in range(max_len):
        yield a
        a, b, c = b, c, a + b + c


N = int(input())

print(*balak_seq(N))
