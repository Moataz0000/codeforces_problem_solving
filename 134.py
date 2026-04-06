def plus_or_minus():

    a, b, c = map(int, input().split())

    if (a + b) == c:
        print("+")
    else:
        print("-")


t = int(input())

while t:
    plus_or_minus()
    t -= 1
