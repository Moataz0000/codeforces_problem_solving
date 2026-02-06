

def sum_conis(arr: list) -> int:
    total = 0
    for i in range(len(arr)):
        total+= arr[i]
    return total


def sort_coins(arr: list) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    biggest = [i for i in arr if i < pivot]
    middle = [x for x in arr if x == pivot]
    smallest = [j for j in arr if j > pivot]

    return sort_coins(smallest) + middle + sort_coins(biggest)



def twins(arr: list):
    my_sum = 0
    counter = 0
    sorted_arr = sort_coins(arr)
    total_sum = sum_conis(arr)

    for coin in sorted_arr:
        my_sum += coin
        counter += 1 
        if my_sum > (total_sum / 2): # is my sum coins bigger then half?
            return counter
        else:
            continue
        

n = int(input())

n_2 = list(map(int, input().split()))

print(twins(n_2))
