



N = int(input().strip())


def rec(n):

    if n == 0:
        return 0
    rec(n - 1)
    print(n)


rec(N)