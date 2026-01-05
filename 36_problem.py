


def print_divisors(n, i=1):
    if i > n: # Base case
        return
    if n % i == 0:
        print(i)
    print_divisors(n, i + 1)


N = int(input("Enter a number: "))
print_divisors(N)
