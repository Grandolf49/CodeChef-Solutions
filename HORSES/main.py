test_case = int(input())
for test in range(test_case):
    size = int(input())
    arr = list(map(int, input().split()))
    for i in range(size):
        arr[i] = int(arr[i])
    arr.sort()
    mini = abs(arr[0] - arr[1])
    for i in range(1, size - 1):
        t = abs(arr[i] - arr[i + 1])
        if t < mini:
            mini = t
    print(mini)
