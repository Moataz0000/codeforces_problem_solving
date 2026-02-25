


def lucky_numbers(n: int) -> str:
    counter = 0
    lucky_numbers = [4, 7]

    for i in str(n):
        if i == "4" or i == "7":
            counter += 1

    if counter in lucky_numbers:
        return "YES"
    else:
        return "NO"

    
n = int(input())
results = lucky_numbers(n)
print(results)