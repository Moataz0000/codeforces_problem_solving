def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False


N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

for _ in range(Q):
    X = int(input())
    if binary_search(A, X):
        print("found")
    else:
        print("not found")
