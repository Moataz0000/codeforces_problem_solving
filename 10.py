




def summation(a):
    sumations = 0
    for i in a:
        sumations += i
    print(abs(sumations))

N = int(input())
A = list(map(int, input().split()))
summation(A)