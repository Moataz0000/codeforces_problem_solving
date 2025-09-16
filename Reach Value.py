


# first Base Case in recursive ?

def canReach(n: list):
    if n == 1:
        return True
    if n % 10 == 0 and canReach(n // 10):
        return True
    if n % 20 == 0 and canReach(n // 20):
        return True
    return False



T = int(input())
for _ in range(T):
    N = int(input())
    print("YES" if canReach(N) else "NO")