



def get_position(*, arr: list) -> None:
    target_num: int = 10

    for i in range(len(arr)):
        if arr[i] <= target_num:
             print(f"A[{i}] = {arr[i]}")



N = int(input())
A = list(map(int, input().split()))

get_position(arr=A)



"""
- Input: 
5
1 2 100 0 30

- Output
A[0] = 1
A[1] = 2
A[3] = 0
"""