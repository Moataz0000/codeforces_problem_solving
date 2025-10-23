


def reversing(arr: list) -> list:
    return arr[::-1]


N = int(input())
A = list(map(int, input().split()))

print(*reversing(A))