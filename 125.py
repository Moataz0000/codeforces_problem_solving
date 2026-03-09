def yes_or_yes(s: str) -> str:
    target = "yes"
    if s.lower() == target:
        return "YES"
    return "NO"


t = int(input())
while t:
    s = input()
    print(yes_or_yes(s))
    t -= 1
