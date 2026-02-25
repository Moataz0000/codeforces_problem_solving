
def who_won(n: int, s: str) -> str:
    s = s.upper()
    anton_score = 0
    danik_score = 0

    for x in s:
        if x == "A":
            anton_score += 1
        if x == "D":
            danik_score += 1

    if anton_score > danik_score:
        return "Anton"
    if anton_score == danik_score:
        return "Friendship"
    return "Danik"

n = int(input())
s = input()

result = who_won(n, s)
print(result)