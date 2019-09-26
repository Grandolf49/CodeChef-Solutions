arr = input().split()
with_draw = int(arr[0])
balance = float(arr[1])
if with_draw % 5 == 0 and (float(with_draw) + 0.5) <= balance:
    balance -= with_draw
    balance -= 0.5
print(balance)
