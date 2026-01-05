
N = int(input().strip())

numbers = list(map(int, input().split()))


def get_max_and_min(arr: list):
    print(min(arr), max(arr))



get_max_and_min(numbers)