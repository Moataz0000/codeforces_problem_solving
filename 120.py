
"""
1 - Rule A: If the number ends in a zero, remove that zero (divide by 10).
2 - Rule B: If the number does not end in a zero, subtract 1.
"""



def subtraction(n: int, k: int) -> int:
    for _ in range(k):
        if n % 10 == 0:
            n = n // 10
        else:
            n = n - 1
    return n

n, k = map(int, input().split())
print(subtraction(n,k))
