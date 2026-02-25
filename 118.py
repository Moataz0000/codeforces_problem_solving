


def search_easy_problem(n: int, N: list[int]):
    for x in N:
        if x == 1:
            return "HARD"
    return "EASY"

n = int(input())
N = list(map(int, input().split()))
print(search_easy_problem(n, N))
