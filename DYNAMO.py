test_case = int(input())

while test_case != 0:
    test_case -= 1
    n = int(input())
    a = int(input())
    n9 = pow(10, n) - 1
    s = a + 2 * n9 + 2
    print(s, flush=True)

    b = int(input())
    c = n9 - b + 1
    print(c, flush=True)

    d = int(input())
    e = n9 - d + 1
    print(e, flush=True)

    op = int(input())

    if op == -1:
        break
