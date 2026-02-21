




def soldier_and_banana(costs: int, dollars: int, bananas: int):
    total_cost = (bananas * (bananas + 1) // 2) * costs 
    borrow = total_cost - dollars
    return borrow if borrow > 0 else 0

k, n, w = map(int, input().split())
result = soldier_and_banana(k, n, w)
print(result)