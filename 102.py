





def arr_coloring(arr: list):
    sum_of_arr = 0
    for i in arr:
        sum_of_arr += i
    if sum_of_arr % 2 == 0:
        print("YES")
    else:
        print("NO")

t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split()))
    arr_coloring(a)
    t -= 1


