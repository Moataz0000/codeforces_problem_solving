


def fucking_program(p: str):
    commands = ['H', 'Q', '9']
    for i in p:
        if i in commands:
            return "YES"
    return "NO"

p = input()
print(fucking_program(p))