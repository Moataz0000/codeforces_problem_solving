

def has_duplicates(arr: list) -> bool: # O(n) instead of O(n2)
    seen = set()

    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False

print(has_duplicates(arr=[1,2,3, 3]))