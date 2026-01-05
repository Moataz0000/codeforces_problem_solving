
correct_password: int = 1999

while True:
    x = int(input().strip())
    if x == correct_password:
        print("Correct")
        break
    else:
        print("Wrong")