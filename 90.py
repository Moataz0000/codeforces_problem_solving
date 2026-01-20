



def is_palindrome(x: int) -> bool:
    x = str(x)
    return x[::-1] == x


x = int(input())
result = is_palindrome(x)
print(result)