test_case = int(input())

for test in range(test_case):
    A = input()
    B = input()
    a = int(A, 2)
    b = int(B, 2)
    # a_or_b = a + b
    # a_and_b = a & b
    c = 0
    while b > 0:
        u = a ^ b
        v = a & b
        if v == 0:
            c += 1
            break
        a = u
        b = v << 1
        c += 1
    print(c)
