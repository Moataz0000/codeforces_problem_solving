


def divisibility(a: int, b: int) -> int:
    result = a % b
    if result == 0:
        return 0
    return b - result


t = int(input())
while t:
    a, b = map(int, input().split())
    print(divisibility(a,b))
    t -= 1