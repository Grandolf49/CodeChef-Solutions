(a, n, k) = map(int, input().split())
ans = []
for i in range(k):
    if n > 0:
        d = a % (n + 1)
        ans.append(d)
        a = int(a / (n + 1))
    else:
        ans.append(0)
for i in range(k):
    print(ans[i], end=' ')
