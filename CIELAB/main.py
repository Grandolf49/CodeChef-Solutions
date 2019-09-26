a, b = input().split()
a = int(a)
b = int(b)
diff = a - b
if diff % 10 != 9:
    print(diff + 1)
else:
    print(diff - 1)
