

# The goal is to figure out the exact year his weight finally passes Bob's



def bear_and_big_brother(a, b):
    count_of_year = 0

    while a <= b:
        a *= 3
        b *= 2
        
        count_of_year += 1
    return count_of_year


a, b = map(int, input().split())
result = bear_and_big_brother(a,b)
print(result)