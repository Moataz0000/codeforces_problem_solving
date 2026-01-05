



def reversing(a: list):
    for i in range(len(a)):
        if a[i] == 0:
            a[:i] = reversed(a[:i])

    return a

N = int(input())
A = list(map(int, input().split()))

print(*reversing(A))