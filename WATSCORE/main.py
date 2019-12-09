test_case = int(input())
for test in range(test_case):
    n = int(input())
    score = 0
    scores = {}
    for i in range(n):
        (p, s) = map(int, input().split())
        if 1 <= p <= 8:
            cur_max = scores.get(p, -1)
            if cur_max == -1:
                score += s
                scores[p] = s
            else:
                if s > cur_max:
                    score += (s - cur_max)
                    scores[p] = s
    print(score)
