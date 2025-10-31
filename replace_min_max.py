

class Solution:
    def __init__(self, arr: list):
        self.arr = arr

    def is_empty(self):
        return len(self.arr) == 0

    def find_min(self):
        if self.is_empty():
            return False
        
        min_value = self.arr[0]
        for num in self.arr:
            if num < min_value:
                min_value = num
        return min_value

    def find_max(self):
        if self.is_empty():
            return False
        
        max_value = self.arr[0]
        for num in self.arr:
            if num > max_value:
                max_value = num
        return max_value

    def replacement(self):
        if self.is_empty():
            return False
        min_value = self.find_min()
        max_value = self.find_max()
        for i in range(len(self.arr)):
            if self.arr[i] == min_value:
                self.arr[i] = max_value
            elif self.arr[i] == max_value:
                self.arr[i] = min_value
        return self.arr   



N = int(input())
A = list(map(int, input().split()))

obj = Solution(arr=A)
result = obj.replacement()
print(*result)
