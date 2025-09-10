


N = int(input().strip())



def print_N(n):
    result = []
    for i in range(1, N + 1):
        result.append(i)
    print(*result)



print_N(N)