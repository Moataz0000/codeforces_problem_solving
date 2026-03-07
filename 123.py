"""
The Rule: 
    - If the two numbers are different, write 1.

    - If the two numbers are the same, write 0.
"""


def compare_numbers(num1: str, num2: str) -> str:
    result = []

    for i in range(len(num1)):
        if num1[i] != num2[i]:
            result.append("1")
        else:
            result.append("0")
    return "".join(result)

n1 = input().strip()
n2 = input().strip()
print(compare_numbers(n1, n2))



