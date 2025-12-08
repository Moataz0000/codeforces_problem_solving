





def new_array(a: list, b: list) -> list:
    C = [*b, *a]
    return C


N = int(input())
A = list(input().split())
B = list(input().split())

print(*new_array(A,B))