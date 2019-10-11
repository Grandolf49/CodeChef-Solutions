test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    inp = [1000, 1000, 1000, 1000, 1000]
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        inp.append(arr[i])
    c = 1

    for i in range(6, len(inp)):
        if (inp[i] < inp[i - 1] and inp[i] < inp[i - 2] and inp[i] < inp[i - 3] and inp[i] < inp[i - 4] and inp[i] <
                inp[i - 5]):
            c += 1

    print(c)
