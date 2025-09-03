
from typing import List


class Solution(object):
    def longestCommonPrefix(self, strs: List[str]):
        perf = strs[0]
        perf_len = len(str)

        for i in strs[1:]:
            while perf != i[0: perf_len]:
                perf_len
            


            print(i)

        

obj = Solution()
obj.longestCommonPrefix(["flower","flow","flight"])