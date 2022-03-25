# 월간 코드 챌린지 시즌3
# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    v = n-1
    for i in range(2, v+1):
        if(v % i == 0):
            return i

n = [
    10,
    12
]

result = [
    3,
    11
]

for q in [0,1]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')