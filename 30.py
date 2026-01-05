

"""
My target to get the lowset num and its position.
"""


def find_lowset(arr: list):
    lowest = min(arr)
    position = arr.index(lowest) + 1
    return lowest, position



N = int(input())
A = list(map(int, input().split()))

print(*find_lowset(A))