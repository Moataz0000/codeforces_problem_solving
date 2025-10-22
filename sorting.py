


def sorting(arr: list):
    if len(arr) < 2:
        return arr 
    else:
        pivot = arr[0]
        less_numbers = [i for i in arr[1:] if i <= pivot]
        greater_numbers = [x for x in arr[1:] if x > pivot]

        return sorting(less_numbers) + [pivot] + sorting(greater_numbers)
    



N = int(input())
A = list(map(int, input().split()))
print(*sorting(A))