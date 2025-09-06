


N = int(input().strip())

number = list(map(int, input().split()))


def recursion_sum(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + recursion_sum(arr, n - 1)




print(recursion_sum(number, N))