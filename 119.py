



def drink_juice(n :int, N: list[int]) -> float:
    summation = 0

    for i in N:
        summation += i
    
    avg = summation / n
    return avg

n = int(input())
N = list(map(int, input().split()))
print(drink_juice(n, N))