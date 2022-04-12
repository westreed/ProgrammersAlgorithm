# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    num    = 0
    for i in range(1,n+1):
        num += x
        answer.append(num)
    return answer

x = [
    2,
    4,
    -4
]

n = [
    5,
    3,
    2
]

result = [
    [2,4,6,8,10],
    [4,8,12],
    [-4,-8]
]

for q in [0,1,2]:
    qid = solution(x[q], n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')