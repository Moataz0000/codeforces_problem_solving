

def calculate_fun(n: int):
    if n % 2 == 0:
        print(int(n / 2))
    else:
        print(int(-(n + 1) / 2))

n = int(input())
calculate_fun(n)