


def string(a, b):
    size_a = len(a)
    size_b = len(b)
    produced = f"{a}{b}"
    reversed_produced = f"{b[0]}{a[1:]} {a[0]}{b[1:]}"
    print(size_a, size_b)
    print(produced)
    print(reversed_produced)

A = input()
B = input()

string(A, B)