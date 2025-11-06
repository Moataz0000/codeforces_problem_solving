



def _solve(s: str):
    prefix = '\\'
    result = []
    for c in s:
        if c == prefix:
            break
        result.append(c)
    return ''.join(result)

S = input()
print(_solve(S))
