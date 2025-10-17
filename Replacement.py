
class Checks:
    def is_positive_number(self, num: int) -> bool:
        return num > 0

    def is_negative_number(self, num) -> bool:
        return num < 0




def replacement(a):
    check = Checks()
    for i in range(len(a)):
        if check.is_positive_number(a[i]):
            a[i] = 1
        elif check.is_negative_number(a[i]):
            a[i] = 2
        else:
            a[i] = 0
    print(*a)

N = int(input())
A = list(map(int, input().split()))
replacement(A)