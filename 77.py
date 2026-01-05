def is_odd(n):
    return n % 2 != 0

def is_palindrome_binary(n):
    b = bin(n)[2:]       # convert to binary string without '0b'
    return b == b[::-1]  # check if palindrome

def check_number(n):
    return "YES" if is_odd(n) and is_palindrome_binary(n) else "NO"

# Main
N = int(input().strip())
print(check_number(N))
