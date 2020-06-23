import math

test = int(input())
for I in range(test):
    size = int(input())
    array = input()
    array = array.split(' ')
    array = list(map(int, array))
    total = sum(array)
    avg = total / size
    mini = math.inf
    idx = -1
    for i in range(size):
        new_avg = total - array[i]
        new_avg = float(new_avg / (size - 1))
        if float(avg) == float(new_avg):
            if array[i] < mini:
                idx = i + 1
                mini = array[i]
    if mini == math.inf:
        print("Impossible")
    else:
        print(idx)
