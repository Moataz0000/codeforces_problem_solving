


def lucky_division(n: int) -> bool:
    lucky_division = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    for i in lucky_division:
        if n % i == 0:
            return True
    return False

n = int(input())
if lucky_division(n):
    print("YES")
else:
    print("NO")