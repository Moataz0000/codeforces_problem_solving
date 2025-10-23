


class Solution:

    def is_palindrome(self, arr: list) -> bool:
        return "YES" if arr == arr[::-1] else "NO"





N = int(input())
A = list(map(int, input().split()))
obj = Solution()
print(obj.is_palindrome(A))