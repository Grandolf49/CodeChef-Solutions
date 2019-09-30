test_cases = int(input())
for test in range(test_cases):
    (n, m) = map(int, input().split())
    inp = list(map(int, input().split()))
    arr = [0] * (n + 1)
    flag = 0
    for i in range(m):
        val = arr[inp[i]] + 1

        for j in range(1, n + 1):
            if inp[i] != j:
                if abs(val - arr[j]) > 1:
                    flag = 1
                    break
        if flag == 0:
            arr[inp[i]] += 1
        else:
            break

    if flag == 0:

        print('YES')
    else:
        print('NO')
