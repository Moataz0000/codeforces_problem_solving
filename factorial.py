def factorial(number: int) -> int:
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

# Read number of test cases
T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    fac = factorial(N)
    print(fac)
