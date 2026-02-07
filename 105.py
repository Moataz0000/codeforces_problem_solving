


def next_round(arr: list, k: int):
    k_th = arr[k-1]

    counter = 0
    for i in range(len(arr)):
        if arr[i] >= k_th and arr[i] > 0:
            counter += 1
    return counter

 
n, k = map(int, input().split())
n_arr = list(map(int, input().split()))

result = next_round(n_arr, k)
print(result)