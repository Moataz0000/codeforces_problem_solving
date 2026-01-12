



def get_len(array: list) -> int:
    counter = 0
    for _ in array:
        counter += 1
    return counter

def num_of_distinct(a: list):
    unique_values: list = []

    for i in a:
        if i not in unique_values:
            unique_values.append(i)
        else:
            continue
    return get_len(unique_values)



N = int(input())
if N == 0:
    print(0)
else:
    A = list(map(int, input().split()))
    print(num_of_distinct(A))


