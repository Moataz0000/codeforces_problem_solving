

def greedy_algorithm():
    data = [1, 4, 2, 5, 6, 7]
    data.sort()

    counter = 0

    for item in data:
        if item % 2 == 0:
            counter += 1
    return counter

# print(greedy_algorithm())


def min_coins(n: int) -> int:
    coins = [100, 20, 10, 5, 1]
    count = 0

    for coin in coins:
        count += n // coin
        n %= coin
    return count

print(min_coins(n=125))