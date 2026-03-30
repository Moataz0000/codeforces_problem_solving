


def smart_sum() -> str:
    a, b, c = map(int, input().split())

    if a + b == c or a + c == b or b + c == a:
        print("YES")
    else:
        print("NO")

t = int(input())
while t:
    smart_sum()
    t -= 1
