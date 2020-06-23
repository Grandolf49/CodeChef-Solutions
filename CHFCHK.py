test_case = int(input())
while test_case != 0:
    test_case -= 1

    n = int(input())
    arr = list(map(int, input().split()))

    print(min(arr))
