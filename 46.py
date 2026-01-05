def print_digits(n):
    if n < 10:
        print(n, end='')
        return
    print_digits(n // 10)
    print(f" {n % 10}", end='')

def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        N = int(data[index])
        index += 1
        print_digits(N)
        print()

if __name__ == "__main__":
    main()