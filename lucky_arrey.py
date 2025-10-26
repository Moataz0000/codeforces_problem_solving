


class Solution:

    def is_odd(self, num: int) -> bool:
        return num % 2 != 0
    
    def lucky_arrey(self, arr: list):
        min_num = min(arr)
        freq = arr.count(min_num)
        if self.is_odd(freq):
            return "Lucky"
        else:
            return "Unlucky"



N = int(input())
A = list(map(int, input().split()))

obj = Solution()
print(obj.lucky_arrey(A))
