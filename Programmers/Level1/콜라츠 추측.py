# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution (num):
    cnt = 0
    while True:
        if num == 1: return cnt
        if cnt > 500: return -1

        num = num / 2 if num % 2 == 0 else num*3 + 1
        cnt += 1
        

n = [
    6,
    16,
    626331
]

result = [
    8,
    4,
    -1
]

for q in [0,1,2]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')