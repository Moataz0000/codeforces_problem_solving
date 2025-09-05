



def recursion_space(n):
    if n == 1:
        print(n, end='')
        return
    print(n, end=' ')
    recursion_space(n - 1)

N = int(input())
recursion_space(N)