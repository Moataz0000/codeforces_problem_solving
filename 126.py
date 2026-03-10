


def be_the_guy(x: list[int], y: list[int], n: int) -> str:
    unique_levels = set(x[1:]) | set(y[1:])
    if len(unique_levels) == n:
        return "I become the guy."
    return "Oh, my keyboard!"

N = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

print(be_the_guy(X, Y, N))


