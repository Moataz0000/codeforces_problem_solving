import math


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False


    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True

T = int(input())

for i in range(T):
    user_input = int(input())
    print("YES" if is_prime(user_input) else "NO")