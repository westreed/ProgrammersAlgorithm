# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k, d):
    dd = d*d
    a = 0
    for y in range(0,d+1,k):
        v = (dd-(y**2))**0.5
        a += v // k + 1
    return int(a)

k = [2, 1]
d = [4, 5]
result = [6, 26]

for q in [0,1 ]:
    qid = solution(k[q], d[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')