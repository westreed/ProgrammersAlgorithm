# 5215
# 연습문제

# 입력
'''
1
5 1000
100 200
300 500
250 300
500 1000
400 400

1
20 1000
100 1
300 2
250 3
500 4
400 5
100 1
300 2
250 3
500 4
400 5
100 1
300 2
250 3
500 4
400 5
100 1
300 2
250 3
500 4
400 5

답
#1 750
'''

testcase = int(input())
answer = ""

for tc in range(testcase):
    N, L = map(int, input().split())
    material = [list(map(int, input().split())) for _ in range(N)]

    score = 0
    from itertools import combinations
    for n in range(1,N+1):
        for res in combinations(material, n):
            calory = sum(map(lambda x : x[1], res))
            if calory <= L:
                _score = sum(map(lambda x : x[0], res))
                if score < _score:
                    score = _score

    answer += f"#{tc+1} {score}\n"

print(answer)