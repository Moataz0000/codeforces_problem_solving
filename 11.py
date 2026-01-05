


X, Y = map(int, input().split())

def add(x, y):
    if x == 0 or y == 0:
        return 0
    x + y
    return add(x, y)


print(add(X, Y))