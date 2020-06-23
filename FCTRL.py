test = int(input())
for i in range(test):
    num = int(input())
    ans = 0
    j = 1
    rem = num
    while rem != 0:
        div = pow(5, j)
        rem = int(num / div)
        ans += rem
        j += 1
    print(ans)
