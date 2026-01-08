


def is_body_equilibrium(z,y,x):
    if z == 0 and y == 0 and x == 0:
        print("YES")
    else:
        print("NO")

def solve():
    try:
        n = int(input())
    except EOFError:
        return
    
    sum_x = 0
    sum_y = 0
    sum_z = 0   

    for _ in range(n):
        x, y, z = map(int, input().split())

        sum_x += x
        sum_y += y
        sum_z += z
    
    is_body_equilibrium(sum_x, sum_y, sum_z)



solve()