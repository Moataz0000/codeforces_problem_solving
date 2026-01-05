




def sum_digits(arr: list) -> int:
    total_sum: int = 0
    for i in arr:
        total_sum += i
    return total_sum
        
N = int(input())
A = list(map(int, input()))

print(sum_digits(A))