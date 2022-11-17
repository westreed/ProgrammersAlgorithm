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

답
#1 750
'''

testcase = int(input())
answer = ""

for tc in range(testcase):
    N, L = map(int, input().split())
    material = [list(map(int, input().split())) for _ in range(N)]

    score = []
    queue = []
    for n in range(N):
        sc, ca = material[n]
        queue.append((sc, ca, [True if n == i else False for i in range(N)]))

    print(queue)
    while queue:
        _score, _calory, _visit = queue.pop(0)
