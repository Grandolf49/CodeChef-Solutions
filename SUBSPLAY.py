test_case = int(input())
for test in range(test_case):
    n = int(input())
    A = input()
    idx = {}
    ans = {}
    least = n
    for i in range(n):
        c = idx.get(A[i])
        if c is None:
            idx[A[i]] = i
            ans[A[i]] = n
        else:
            a = ans.get(A[i])
            b = i - c
            idx[A[i]] = i
            if b < a:
                if b < least:
                    least = b
                ans[A[i]] = b
    print(n - least)

'''
Test Cases
1
9
abcdbdcad
1
11
cbdbadbcbda
1
12
cbdbadbcbcda
1
9
abcdbcdbd
Output
7
9
10
7
'''
