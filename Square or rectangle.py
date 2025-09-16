



T = int(input().strip())

numbers = list(map(int, input().split()))


for num in numbers:
    if num == num + 1:
        print("Square")
    else: 
        print("Rectangle")

