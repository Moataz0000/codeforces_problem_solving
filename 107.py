"""
Rule 1:
- Look at the first letter.
- The word with the earlier alphabet letter wins.

Rule 2 (only if first letters match):
- Move to the next letter.
- Compare again.

Rule 3:
- If one word ends first, the shorter one comes first.
"""


def lexicographically(s1: str, s2: str):
    s1, s2 = s1.lower(), s2.lower()

    for i in range(len(s1)):
        if s1[i] < s2[i]:
            return -1
        elif s1[i] > s2[i]:
            return 1

    return 0

s1 = input()
s2 = input()

result = lexicographically(s1, s2)
print(result)

