


def get_power(base: int, exp: int) -> int:
    result = 1
    for _ in range(exp):
        result *= base
    return result

line = input().split()
X = int(line[0])
N = int(line[1])

total_sum = 0


for i in range(0, N+1, 2):
    if i == 0:
        total_sum += (get_power(X, 0) - 1)
    else:
        total_sum += get_power(X, i)

print(total_sum)