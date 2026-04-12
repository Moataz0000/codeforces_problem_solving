


def two_sisters(n: int):
    result = (n - 1) // 2
    print(result)

t = int(input())

while t:
    n = int(input())
    two_sisters(n)
    t -= 1
