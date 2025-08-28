



N = input().strip()


def is_palindrome(n):
    reversed_N = n[::-1]
    without_zero = reversed_N.strip("0")
    print(without_zero)
    if n == reversed_N:
        print("YES")
    else: print("NO")

is_palindrome(N)