import math

test_case = int(input())
for test in range(test_case):
    (a, b) = map(int, input().split())
    n = abs(a - b)
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # If divisors are equal,
            # count only one
            if n / i == i:
                cnt = cnt + 1
            else:  # Otherwise count both
                cnt = cnt + 2
    if cnt == 0:
        print(-1)
    else:
        print(cnt)
