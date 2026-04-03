import math

def taxi():
    n = int(input())
    s = list(map(int, input().split()))

    count_1 = s.count(1)
    count_2 = s.count(2)
    count_3 = s.count(3)
    count_4 = s.count(4)

    taxis = 0

    taxis += count_4

    taxis += count_3
    count_1 = max(0, count_1 - count_3)

    taxis += count_2 // 2

    if count_2 % 2 == 1:
        taxis += 1
        count_1 = max(0, count_1 - 2)

    taxis += math.ceil(count_1 / 4)

    return taxis

print(taxi())