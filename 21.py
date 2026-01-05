import sys

def is_odd(num) -> bool:
    return num % 2 != 0

N = int(input().strip())

if N == 0 or not is_odd(N):
    sys.exit(1)

for i in range(N):
    for j in range(N):
        # افحص تقاطع القطرين أولاً
        if i == j and i + j == N - 1:
            print('X', end='')
        elif i == j:
            print('\\', end='')
        elif i + j == N - 1:
            print('/', end='')
        else:
            print('*', end='')
    print()
