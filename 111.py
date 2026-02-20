


def min_num_of_step(distance: int) -> int:
    steps = distance // 5
    if distance % 5 != 0:
        steps += 1 
    return steps


x = int(input())
result = min_num_of_step(x)
print(result)