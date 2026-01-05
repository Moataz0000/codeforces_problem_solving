


N = int(input())
A = map(int, input().split())
X = int(input())

def search(x):
    a = list(A)
    for i in a:
        if x == i:
            print(a.index(i))
            return
    print(-1)


search(X)