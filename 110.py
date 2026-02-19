


def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    left_nums = [i for i in arr if i < pivot] 
    middle_num = [x for x in arr if x == pivot]
    right_nums = [n for n in arr if n > pivot] 

    return quick_sort(left_nums) + middle_num + quick_sort(right_nums)


def extract_only_number(arr: list) -> list[int]:
    numbers = []
    for num in arr:
        if num == "+":
            continue
        numbers.append(num)
    return numbers


def solation(s: str):
    charactars_list = list(s)
    list_of_numbers = extract_only_number(charactars_list)
    sorted_numbers = quick_sort(list_of_numbers)

    operations = []
    for n in sorted_numbers:
        operations.append(n)
        operations.append("+")
    return "".join(operations[:-1])



s = input()
result = solation(s)
print(result)
