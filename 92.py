


# Each number is the sum of the two numbers before it.


def fib(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(3, n + 1):
        current = a + b
        a = b
        b = current
    return current


n = int(input())
result = fib(n)

print(result)