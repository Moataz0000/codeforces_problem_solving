


def find_max_dominoes(m: int, n: int) -> int:
    max_dominoes_found = (m * n) // 2
    return max_dominoes_found

M, N = map(int, input().split())
result = find_max_dominoes(M, N)
print(result)