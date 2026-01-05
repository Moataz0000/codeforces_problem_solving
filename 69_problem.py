

S = input()
N = int(input())

def histogram(s, n):
    numbers = list(map(int, input().split()))
    for i in numbers:
        print(f"{S * i}")
    return



histogram(s=S, n=N)


