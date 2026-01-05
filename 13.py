
def _avg(a: list) -> None:
    result = 0
    for i in range(len(a)):
        result += a[i] / len(a)
    print(f"{result:.6f}")

N = input()
A = list(map(float, input().split()))
_avg(a=A)