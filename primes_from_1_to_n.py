import math

N = int(input().strip())


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

primes_numbers = []
for number in range(1, N + 1):
    if is_prime(number):
        primes_numbers.append(number)
print(*primes_numbers)