def some_sums(*, n: int, a: int, b: int) -> int:
    total: int = 0
    for i in range(1, n + 1):
        sum_digits = sum(int(d) for d in str(i))

        if a <= sum_digits <=b:
            total += i
    return total

N, A, B = map(int, input().split())
fun = some_sums(n=N, a=A, b=B)
print(fun)
