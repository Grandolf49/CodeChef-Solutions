test = int(input())
while test != 0:
    test -= 1
    (n, w1, w2, w3) = map(int, input().split())
    sum1 = w1 + w2 + w3
    if sum1 <= n:
        print(1)
    elif w1 + w2 <= n or w2 + w3 <= n:
        print(2)
    else:
        print(3)
