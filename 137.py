



# def find_pair_with_sum(arr: list, target: int) -> bool:
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 return True
#     return False


# print(find_pair_with_sum(arr=[1,2,3], target=3))


def find_pair_with_sum(arr: list, target: int) -> bool:

    left, right = 0, len(arr) - 1 # first and last indexs

    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return True
        elif s < target: # less then
            left += 1 # move one step
        else:
            right -= 1 # miunse one step
    return False

print(find_pair_with_sum(arr=[1,2,3], target=3))









