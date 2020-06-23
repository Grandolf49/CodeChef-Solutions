test_case = int(input())
while test_case != 0:
    test_case -= 1

    (n, a, b, c) = map(int, input().split())
    f = list(map(int, input().split()))

    ans = abs(b - f[0]) + c + abs(a - f[0])
    for i in range(0, n):
        temp = abs(b - f[i]) + c + abs(a - f[i])
        if temp < ans:
            ans = temp

    print(ans)
