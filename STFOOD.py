import math

test_case = int(input())
while test_case != 0:
    test_case -= 1

    n = int(input())
    s = []
    p = []
    v = []

    for i in range(n):
        (s1, p1, v1) = map(int, input().split())
        s.append(s1)
        p.append(p1)
        v.append(v1)

    ans = -1
    for i in range(n):
        temp = math.floor(p[i] / (s[i] + 1))
        temp *= v[i]
        if temp > ans:
            ans = temp

    print(ans)
