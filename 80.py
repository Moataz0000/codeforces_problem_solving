


def palindromes_replace(s: str):
    chars = list(s)
    print(chars)
    n = len(chars)

    for i in range(n // 2):
        left = i
        right = n - 1 - i

        if chars[left] != '?' and chars[right] != '?' and chars[left] != chars[right]:
            print("-1")
            return
        
        if chars[left] == '?' and chars[right] == '?':
            chars[left] = chars[right] = 'a'
        elif chars[left] == '?':
            chars[left] = chars[right]
        elif chars[right] == '?':
            chars[right] = chars[left]
    
    if n % 2 != 0:
        mid = n // 2
        if chars[mid] == '?':
            chars[mid] = 'a'
    print("".join(chars))




S = input()
palindromes_replace(S)