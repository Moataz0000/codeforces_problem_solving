



def arr_coloring(arr: list):
    result = 0
    for i in arr:
        result += i
    if result % 2 == 0:
        print("YES")
    else:
        print("NO")

t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split()))
    arr_coloring(a)
    t -= 1

    
