


N = int(input().strip())


def recursion(n):
    if n == 0: # Base Case
        return 0
    
    print("I love Recursion")

    return recursion(n - 1)

recursion(n=N)