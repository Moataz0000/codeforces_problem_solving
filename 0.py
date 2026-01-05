


n, k, a = map(int, input().split())

if abs(n * k / a - int(n * k / a)) > 1e-9:
    print("double")

else:
    if (n % a == 0):
        temp = n // a
        result = temp * k
    elif (k % a == 0):
        temp = k // a
        result = temp * n
    else:
        import math
        gcd1 = math.gcd(n, a)
        simplified_n = n // gcd1
        simplified_a = a // gcd1
        gcd2 = math.gcd(k, simplified_a)
        simplified_k = k // gcd2
        simplified_a_final = simplified_a // gcd2
        if simplified_a_final == 1:
            result = simplified_n * simplified_k
        else:
            result = (n * k) // a 

    if -2147483648 <= result <= 2147483647:
        print("int")
    else:
        print("long long")