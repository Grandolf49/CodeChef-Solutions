test_case = int(input())
for test in range(test_case):
    (n, m, k, l, r) = map(int, input().split())
    c = []
    p = []
    for i in range(n):
        (a, b) = map(int, input().split())
        c.append(a)
        p.append(b)

    isSolExist = False
    sol_list = []
    for i in range(n):
        final_temp = c[i]
        if c[i] < k:
            final_temp = c[i] + m
            if final_temp > k:
                final_temp = k
        if c[i] > k:
            final_temp = c[i] - m
            if final_temp < k:
                final_temp = k
        if r >= final_temp >= l:
            isSolExist = True
            sol_list.append(p[i])

    if len(sol_list) == 0:
        print(-1)
    else:
        sol_list.sort()
        print(sol_list[0])
