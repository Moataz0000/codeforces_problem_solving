import time
import random


def qsort(arr: list) -> list:

    if len(arr) < 2: # Base Case
        return arr
    
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]  
    greater = [i for i in arr[1:] if i > pivot]  
    
    return qsort(less) + [pivot] + qsort(greater)  

    

unsorted_list = [random.randint(1, 1000000000) for _ in range(1000)]

start = time.perf_counter()
q = qsort(arr=unsorted_list)
elapsed = time.perf_counter() - start


print(f"Elapsed time for qsort on 1000 ints: {elapsed*1000:.3f} ms")
print("Matches built-in sorted():", q == sorted(unsorted_list))
print(q)