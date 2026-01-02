



def get_unique_value(*, array: list):
    unique_values: set = set()
    duplicated_values: set = set()

    for i in array:
        if i in unique_values:
            duplicated_values.add(i)
        else:
            unique_values.add(i)

    return f"{list(unique_values)} \n{list(duplicated_values)}"
    

array_of_numbers = [1,2,3,4,5,5, 6, 5, 6, 0, 0]
print(get_unique_value(array=array_of_numbers))