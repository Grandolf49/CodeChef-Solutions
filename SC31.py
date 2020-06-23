test_cases = int(input())


def count_set_bits(n1):
    if n1 == 0:
        return 0
    else:
        return (n1 & 1) + count_set_bits(n1 >> 1)


for test in range(test_cases):
    n = int(input())
    array = []
    ans = -1
    for i in range(n):
        arr = int(str(input()), 2)
        array.append(arr)
    ans = array[0]
    for i in range(1, n):
        ans = array[i] ^ ans
    print(count_set_bits(ans))
