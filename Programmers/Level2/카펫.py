# 완전탐색
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    if yellow == 1: return [3,3]
    for i in range(2, yellow+1):
        a,b = divmod(yellow, i)
        if b == 0 and i >= a:
            size = (i+2)*(a+2)
            if brown+yellow == size:
                return [i+2, a+2]

brown = [
    10,
    8,
    24
]

yellow = [
    2,
    1,
    24
]

result = [
    [4, 3],
    [3, 3],
    [8, 6]
]

for q in [0,1,2]:
    qid = solution(brown[q], yellow[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')