

def word_capitalization(word: str) -> str:
    if word[0].upper() == word[0]:
        return word
    return word[0].capitalize() + word[1:]

word = input()
result = word_capitalization(word)
print(result)