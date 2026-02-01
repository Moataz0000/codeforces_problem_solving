

def experssion(a: int,b: int,c: int) -> int:
    result_mapping = {
        "1": a + b + c,
        "2": a * b * c,
        "3": a + (b * c),
        "4": (a + b) * c,
        "5": a * (b + c),
        "6": (a * b) + c
    }

    biggest_result = result_mapping["1"]
    for key, value in result_mapping.items():
        if value > biggest_result:
            biggest_result = value

    return biggest_result

a = int(input())
b = int(input())
c = int(input())
print(experssion(a,b,c))

