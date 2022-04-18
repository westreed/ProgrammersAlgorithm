# 월간 코드 챌린지 시즌1
# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    value = ''
    while(n):
        n, r = divmod(n, 3)
        value = f'{value}{r}'

    return int(value, 3)

n = [
    45,
    125
]

result = [
    7,
    229
]

for q in [0,1]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')