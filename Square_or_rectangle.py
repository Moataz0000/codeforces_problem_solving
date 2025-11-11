



def square_or_rectangle(w: int, h: int):
    if w == h:
        return "Square"
    return "Rectangle"



a = int(input())

for _ in range(a):
    W, H = map(int, input().split())
    print(square_or_rectangle(W,H))


