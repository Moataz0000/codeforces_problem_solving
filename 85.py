


def get_max(arr: list) -> int:
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val

def get_min(arr: list) -> int:
    min_val = arr[0]
    for x in arr:
        if x < min_val:
            min_val = x
    return min_val

def get_prime(arr: list) -> int:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    counter: int = 0
    for n in arr:
        if is_prime(n):
            counter += 1
    return counter
  
def get_palindrome(arr: list) -> int:
    def is_palindrome(num: int) -> bool:
        num = str(num)
        if num == num[::-1]:
            return True
        return False
    
    counter: int = 0
    for n in arr:
        if is_palindrome(n):
            counter += 1
    return counter

    
def get_max_divisors(arr: list) -> int:
    def count_divisore(num: int) -> int:
        counter: int = 0
        for n in range(1, num + 1):
            if num % n == 0:
                counter += 1
        return counter
    
    max_divs: int = -1
    best_num: int = -1

    for i in arr:
        current_divs = count_divisore(i)

        if current_divs > max_divs:
            max_divs = current_divs
            best_num = i
        elif current_divs == max_divs:
            if i > best_num:
                best_num = i
    return best_num
                
    

N = int(input())
A = list(map(int, input().split()))
print(f"The maximum number : {get_max(A)}")
print(f"The minimum number : {get_min(A)}")
print(f"The number of prime numbers : {get_prime(A)}")
print(f"The number of palindrome numbers : {get_palindrome(A)}")
print(f"The number that has the maximum number of divisors : {get_max_divisors(A)}")

