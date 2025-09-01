
N = int(input().strip())

numbers = list(map(int, input().split()))


def getMax(nums: list) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    max_of_rest = getMax(nums[1:])
    return nums[0] if nums[0] > max_of_rest else max_of_rest


print(getMax(numbers))