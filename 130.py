


def pangram_language():
    n = int(input())
    s = input()

    s_normalized = s.lower()
    unique_letters = set(s_normalized)

    print("YES" if len(unique_letters) == 26 else "NO")

pangram_language()