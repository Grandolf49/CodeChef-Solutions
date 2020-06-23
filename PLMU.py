test_case = int(input())
for test in range(test_case):
    n = int(input())
    c0 = 0
    c2 = 0
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] == 0:
            c0 += 1
        if arr[i] == 2:
            c2 += 1
    c = int(c0 * (c0 - 1) / 2) + int(c2 * (c2 - 1) / 2)
    print(c)
