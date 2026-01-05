import math


x = int(input().strip())


def is_prime(n: int):

    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    max_divisor = math.isqrt(n) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True


if is_prime(x):
    print("YES")
else: print("NO")

