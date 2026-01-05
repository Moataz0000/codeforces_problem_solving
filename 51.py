


"""
Take the first item in the arr then recall the fun again
"""

def sumArr(arr: list):
    if not arr:
        return 0
    return arr[0] + sumArr(arr[1:])



ar = [3, 2, 1]
print(sumArr(arr=ar))