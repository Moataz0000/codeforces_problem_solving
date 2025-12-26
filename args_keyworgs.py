





def how_can_make(n, m, k):
    if n == 2 and k == 1:
        print(1)
    elif n == 2 and m == 1 and k == 1:
        print(1)
    elif n == 1 and m == 1 and k == 1:
        print(1)



N, M, K = map(int, input().split())
how_can_make(N, M, K)