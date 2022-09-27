# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    V1 = 1
    V2 = 2

    if n == 1: return V1
    if n == 2: return V2

    for _ in range(n-2):
        Temp = V1
        V1 = V2
        V2 = V1+Temp
    return V2 % 1000000007

n = [4]
result = [5]

for q in [0]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')