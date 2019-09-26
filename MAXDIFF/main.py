test_case = int(input())
for test in range(test_case):
    (n, k) = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    sum_asc_1 = 0
    sum_asc_2 = 0
    sum_dsc_1 = 0
    sum_dsc_2 = 0
    for i in range(n):
        if i < k:
            sum_asc_1 += arr[i]
        else:
            sum_asc_2 += arr[i]

        if i >= (n - k):
            sum_dsc_1 += arr[i]
        else:
            sum_dsc_2 += arr[i]

    diff_asc = abs(sum_asc_1 - sum_asc_2)
    diff_dsc = abs(sum_dsc_2 - sum_dsc_1)

    if diff_dsc > diff_asc:
        print(diff_dsc)
    else:
        print(diff_asc)
