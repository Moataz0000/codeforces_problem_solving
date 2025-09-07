


vowels_latters = ["a", "o", "y", "e", "u", "i"]

word = input().lower()
for i in word:
    if i in vowels_latters:
        continue
    else:
        result = "." + ".".join(i)
        print(result, end='')
