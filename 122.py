


def horseshoe(s1: int, s2: int, s3: int, s4: int) -> int:
    return 4 - len({s1, s2, s3, s4})

s1, s2, s3, s4 = map(int, input().split())
print(horseshoe(s1, s2, s3, s4))