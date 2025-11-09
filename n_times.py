

def print_chars(N, C):
    print((C + " ") * N)

T = int(input())
for _ in range(T):
    N, C = input().split()
    N = int(N)
    print_chars(N, C)
