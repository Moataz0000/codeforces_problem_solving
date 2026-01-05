

N = int(input())
numbers = list(map(int, input().split()))



def recursive_max(arr: list):
    if len(arr) == 1: # Base case
        return arr[0]
    
    rest_max = recursive_max(arr[1:])
    
    if arr[0] > rest_max:
        return arr[0] # found the max number
    else:
        return rest_max
    


print((recursive_max(numbers)))
