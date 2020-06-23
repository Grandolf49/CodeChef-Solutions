test_cases = int(input())
for test in range(test_cases):
    G = int(input())
    for g in range(G):
        (i, n, q) = map(int, input().split())
        ans = int(n / 2)
        if i == q:
            print(ans)
        else:
            print(n - ans)
