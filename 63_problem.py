class Solution(object):
    def isValid(self, s):
        valid = ["[]", "{}", "()", "()[]{}", "([])", "{[]}"]
        if s not in valid:
            return False
        return True 
    


obj = Solution()
obj.isValid("()")

