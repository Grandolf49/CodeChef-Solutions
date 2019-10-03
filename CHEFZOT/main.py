n = int(input())
inp = list(map(int, input().split()))
max_so_far = 0
curr_length = 0
prod = 1
for i in range(n):
    prod *= inp[i]
    if prod != 0:
        curr_length += 1
    else:
        if curr_length > max_so_far:
            max_so_far = curr_length
        prod = 1
        curr_length = 0
if curr_length > max_so_far:
    max_so_far = curr_length
print(max_so_far)
