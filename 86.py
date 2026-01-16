



def qick_sort(arr: list):
    if len(arr) <= 1: # the best case
        return arr
    
    pivot = arr[len(arr) // 2] # the middel element

    left_nums = [i for i in arr if i < pivot] # smallest nums

    middle_num = [x for x in arr if x == pivot]

    right_nums = [n for n in arr if n > pivot] # biggest nums

    return qick_sort(left_nums) + middle_num + qick_sort(right_nums)


unsorted_list = [2,1,3,4,8,5]

qs = qick_sort(unsorted_list)
print(qs)