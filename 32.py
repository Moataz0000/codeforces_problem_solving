


def generate_lucky_numbers(current, length, results):
    if len(current) == length:
        num = int(current)
        results.append(num)
        return
    generate_lucky_numbers(current + '4', length, results)
    generate_lucky_numbers(current + '7', length, results)


def main():
    A, B = map(int, input().split())
    all_lucky = []
    for length in range(1, 6): 
        generate_lucky_numbers('', length, all_lucky)
    all_lucky.sort()
    lucky_in_range = []
    for num in all_lucky:
        if A <= num <= B:
            lucky_in_range.append(str(num))
    if lucky_in_range:
        print(' '.join(lucky_in_range))
    else:
        print(-1)

if __name__ == '__main__':
    main()