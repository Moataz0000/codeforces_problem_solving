




def translate_to_birland(s: str, t: str):
    if t == s[::-1]:
        print('YES')
        return
    print('NO')



s = input()
t = input()


translate_to_birland(s, t)