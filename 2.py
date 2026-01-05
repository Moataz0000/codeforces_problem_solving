
N = int(input().strip())

numbers = list(map(int, input().split()))

class Solution:

    @staticmethod
    def is_even(nums: list) -> None:
        total = 0
        for num in nums:
            if num % 2 == 0:
                total += 1
        print(f"Even: {total}")

    @staticmethod
    def is_positive(nums: list) -> None:
        total = 0
        for num in nums:
            if num > 0:
                total += 1
        print(f"Positive: {total}")

    @staticmethod
    def is_negative(nums: list) -> list:
        total = 0
        for num in nums:
            if num < 0:
                total += 1
        print(f"Negative: {total}")

    @staticmethod
    def is_odd(nums: list) -> None:
        total = 0
        for num in nums:
            if num % 2 != 0:
                total += 1
        print(f"Odd: {total}")

obj = Solution
obj.is_even(numbers)
obj.is_odd(numbers)
obj.is_positive(numbers)
obj.is_negative(numbers)



