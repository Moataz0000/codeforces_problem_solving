






def shift_right(arr: list, x: int, n: int) -> list:
    x = x % n

    if x == 0:
        return arr
    
    part1 = arr[n-x:]
    part2 = arr[:n-x]

    merged = part1 + part2
    return merged



line = list(map(int, input().split()))
n = line[0]
x = line[1]
arr = list(map(int, input().split()))

result = shift_right(arr, x, n)
print(*result)