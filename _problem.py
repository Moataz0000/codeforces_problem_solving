import math

def get_min(numbers: list) -> int:
    return min(numbers)

def get_max(numbers: list) -> int:
    return max(numbers)

def count_primes(numbers: list) -> int:
    counter = 0
    for num in numbers:
        if num < 2:
            continue
        if num == 2: 
            counter += 1
            continue
        if num % 2 == 0:
            continue

        is_priem = True
        for divisor in range(3, int(math.sqrt(num)) + 1, 2):
            if num % divisor == 0:
                is_priem = False
                break
        if is_priem:
            counter += 1
    return counter
        
def count_palindrome(numbers: list) -> int:
    count = 0
    for num in numbers:
        s = str(abs(num))
        if s == s[::-1]:
            count += 1
    return count

def count_divisors(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def max_divisors_number(numbers: list) -> int:
    max_num = numbers[0]
    max_count = count_divisors(numbers[0])

    for num in numbers[1:]:
        c = count_divisors(num)
        if c >= max_count:
            max_count = c
            max_num = num

    return max_num



def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(f"The maximum number : {get_max(A)}")
    print(f"The minimum number : {get_min(A)}")
    print(f"The number of prime numbers : {count_primes(A)}")
    print(f"The number of palindrome numbers : {count_palindrome(A)}")
    print(f"The number that has the maximum number of divisors : {max_divisors_number(A)}")




if __name__ == "__main__":
    main()