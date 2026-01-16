


def qick_sort(arr: list, reversed_order: bool = False):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    smallest = [i for i in arr if i < pivot]
    middle = [m for m in arr if m == pivot]
    biggest = [x for x in arr if x > pivot]

    if reversed_order:
        return qick_sort(biggest, reversed_order) + middle + qick_sort(smallest, reversed_order)
    return qick_sort(smallest, reversed_order) + middle + qick_sort(biggest, reversed_order)


def get_max_sum(arr: list, k: int):
    sorted_arr = qick_sort(arr, reversed_order=True)
    total_sum = 0
    count = 0

    for i in sorted_arr:
        if count < k and i > 0:
            total_sum += i
            count += 1
        else:
            break
    return total_sum


n, k = map(int, input().split())
a = list(map(int, input().split()))
print(get_max_sum(a, k))
