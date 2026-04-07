



def fist_step(a: list[int]) -> int:
    max_streak = 1
    current_streak = 1

    for i in range(1, len(a)):
        if a[i] >= a[i - 1]:
            current_streak += 1
        else:
            current_streak = 1
        if current_streak > max_streak:
            max_streak = current_streak

    return max_streak

n = int(input())
a = list(map(int, input().split()))

print(fist_step(a))

