def qsort(arr: list) -> list:

    if len(arr) < 2: # Base Case
        return arr
    
    pivot = arr[0] # Recursive Case
    less = [i for i in arr[1:] if i <= pivot]  
    greater = [i for i in arr[1:] if i > pivot]  
    
    return qsort(less) + [pivot] + qsort(greater)  

    
print(qsort([4, 2, 7, 1, 3, 5,10]))

