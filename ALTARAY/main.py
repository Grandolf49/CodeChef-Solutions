test_case = int(input())
for test in range(test_case):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        if i == (n - 1):
            ans[i] = 1
        else:
            prod = arr[i] * arr[i + 1]
            if prod < 0:
                ans[i] = ans[i + 1] + 1
            else:
                ans[i] = 1

    for i in range(len(ans)):
        print(ans[i], end=' ')
    print('')
