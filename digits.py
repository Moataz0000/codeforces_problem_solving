


numbers: list = []
def solve():
    T = int(input().strip())
    for i in range(T):
        num = input().strip()
        numbers.append(num)
    for i in numbers:
        reversed_N = i[::-1]
        result = ' '.join(reversed_N)
        print(result)


if __name__ == "__main__":
    solve()