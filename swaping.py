

def swaping(x, y):
    temp = x 
    x = y
    y = temp
    

    return x, y


X, Y = map(int, input().split())

print(*swaping(X, Y))