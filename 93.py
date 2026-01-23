



def matrix_difference(n: int, arr: list) -> int:
    prime_sum = 0
    second_sum = 0

    for i in range(n):
        prime_sum += arr[i][i]
        second_sum += arr[i][n - 1 - i]

    return abs(prime_sum - second_sum)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

print(matrix_difference(N, A))

