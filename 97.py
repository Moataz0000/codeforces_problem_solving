


def beautiful_year(y: int):
    while True:
        y += 1
        if len(set(str(y))) == len(str(y)):
            return y
        break

y = int(input())
result = beautiful_year(y)
print(result)