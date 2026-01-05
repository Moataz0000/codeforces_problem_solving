


def count_word(s):
    exclude_latters = ['!', '.', '?', ',']
    for i in exclude_latters:
        s = s.replace(i, ' ')
    words = [word for word in s.split() if word.isalpha()]
    return len(words)




S = input()
print((count_word(S)))