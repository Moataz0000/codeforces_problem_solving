
"""
The rules:
    - The pair "BG" becomes "GB".
    - If it is "BB" or "GG" or "GB", nothing happens to that pair in that second.
"""


def queue_swapping() -> str:
    n, t = map(int, input().split())
    s = list(input())

    for _ in range(t):
        i = 0
        while i < n - 1:
            if s[i] == "B" and s[i + 1] == "G":
                s[i], s[i + 1] = "G", "B"

                i += 2
            else:
                i += 1  
    print("".join(s))
    

solve_problem()