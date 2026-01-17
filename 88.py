








n, k = map(int, input().split())
N = list(map(int, input().split()))


for i in range(0, n, k):
    group = N[i : i + k]

    print (min(group), end=" ")