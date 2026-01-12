


def shift_zeros(a: list) -> int:
    non_zeros = [x for x in a if x != 0]
    zeros = [0] * (len(a) - len(non_zeros))
    return non_zeros + zeros





N = int(input())

if N == 0:
    print(0)
else:
    A = list(map(int, input().split()))
    print(*shift_zeros(A))