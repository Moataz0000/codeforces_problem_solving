

def lottery() -> int:
    n = int(input())

    counter = 0
    
    total_100 = n // 100
    counter += total_100
    n %= 100

    total = n // 20
    counter += total
    n %= 20

    total = n // 10
    counter += total
    n %= 10

    total = n // 5
    counter += total
    n %= 5

    total = n // 1
    counter += total
    n %= 1

    return counter

print(lottery())
