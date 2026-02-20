

# Rule: No Twin Neighbors


def stone(n: int, s: str) -> int:
    removal_count = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            removal_count += 1
    return removal_count


n = int(input())
s = input()
result = stone(n, s)
print(result)
