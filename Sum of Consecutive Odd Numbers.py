T = int(input().strip())

def is_odd(n: int) -> bool:
    return n % 2 != 0

for _ in range(T):
    X, Y = map(int, input().split())

    if X > Y:
        X, Y = Y, X

    total = 0
    for i in range(X + 1, Y):
        if is_odd(i):
            total += i
    print(total)
