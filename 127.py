


def minimum_total_distance(x1: int, x2: int, x3: int) -> int:
    return max(x1, x2, x3) - min(x1, x2, x3)


x1, x2, x3 = map(int, input().split())
print(minimum_total_distance(x1, x2, x3))