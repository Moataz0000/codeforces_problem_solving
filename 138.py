

def lottery_greedy(n: int) -> int:
    coins = [100, 20, 10, 5, 1]
    count = 0

    for coin in coins:
        count += n // coin
        n %= coin
    return count

print(lottery_greedy(n=125))