


N = int(input())
numbers = list(map(int, input().split()))

def f(x):
    count = 0
    while x % 2 == 0:
        x //= 2
        count += 1
    return count

max_f = 0
for num in numbers:
    max_f = max(max_f, f(num))

print(max_f)
