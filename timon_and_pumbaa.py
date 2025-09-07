

a, b = map(int, input().split())


def aggre(A: int, B: int) -> None:
    result = A - B
    if result <= 0:
        print(0)
    else:
        print(result)


aggre(a,b)