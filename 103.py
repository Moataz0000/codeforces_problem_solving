



def game_with_int(n):
    if n % 3 != 0:
        print("First")
    elif n % 3 == 0:
        print("Second")

t = int(input())

for _ in range(t):
    n = int(input())
    game_with_int(n)
