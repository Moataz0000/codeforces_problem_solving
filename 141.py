import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    for x in arr:
        root = int(math.isqrt(x))  
        
        if root * root == x and is_prime(root):
            print("YES")
        else:
            print("NO")


solve()
