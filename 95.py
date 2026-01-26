

def is_even(n: int) -> int:
    return bool(n % 2 == 0)

def decoding(n: int, s: str) -> str:
    decoded: list = []

    for i in range(n):
        if is_even(n-i):
            decoded.insert(0, s[i]) 
        else:
            decoded.append(s[i])
    return ("".join(decoded))

n = int(input())
s = input()

print(decoding(n, s))


