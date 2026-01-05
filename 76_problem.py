from typing import List


list_1 = [5, 2, 0, 8]
list_2 = [3, 1, 4, 9]


def merge_2_list(arr_1: list, arr_2: list) -> List[int]:
    return sorted([*arr_1, *arr_2])
print(merge_2_list(list_1, list_2))


