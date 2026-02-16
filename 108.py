


def is_even(n: int) -> bool:
    return bool(n % 2 == 0)


def get_max_operaiton(arr: list) -> int:
   operation_count = 0
   while True:
      for x in arr:
         if not is_even(x): # the num is odd
            return operation_count

      arr = [x // 2 for x in arr]
      operation_count += 1


N = int(input())
A = list(map(int, input().split()))

result = get_max_operaiton(A)
print(result)