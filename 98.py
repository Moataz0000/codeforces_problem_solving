




def iq_test(arr: list[int]):
    def is_even(number: int):
        return bool(number % 2 == 0)
    
    evens = []
    odds = []

    for i in range(len(arr)):
        if is_even(arr[i]):
            evens.append(i)
        else:
            odds.append(i)

    if len(evens) == 1:
        return evens[0] + 1 
    elif len(odds) == 1:
        return odds[0] + 1 

n = int(input())
arr = list(map(int, input().split()))

result = iq_test(arr)
print(result)