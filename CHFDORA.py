test_case = int(input())
while test_case != 0:
    test_case -= 1
    (n, m) = map(int, input().split())
    ans = n * m
    A = []
    for i in range(n):
        t = list(map(int, input().split()))
        A.append(t)

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            k = 1
            while j - k >= 0 and i - k >= 0 and j + k < m and i + k < n:
                l = A[i][j - k]
                r = A[i][j + k]
                u = A[i - k][j]
                d = A[i + k][j]
                if l == r and u == d:
                    ans += 1
                else:
                    break
                k += 1
    print(ans)
