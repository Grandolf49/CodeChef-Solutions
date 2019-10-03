n = int(input())
inp = list(map(int, input().split()))
sum_1 = 0
for i in range(len(inp)):
    sum_1 += inp[i]
if sum_1 == int((n * (n + 1)) / 2):
    print('YES')
else:
    print('NO')
