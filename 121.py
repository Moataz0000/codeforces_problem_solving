


# odd first even second


def even_odds(n: int, k: int):
    wall = (n + 1) // 2
    if k > wall:
        return 2 * (k - wall)
    else:
        return (2 * k) - 1

n, k = map(int, input().split())
print(even_odds(n,k))