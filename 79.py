

def registration_system():
    n = int(input())
    database = {}

    for _ in range(n):
        name = input().strip().lower()

        if name == "" or len(name) > 32:
            raise ValueError("Error")
        
        if name not in database:
            database[name] = 0
            print("OK")
            
        else:
            database[name] += 1
            print(f"{name}{database[name]}")





registration_system()