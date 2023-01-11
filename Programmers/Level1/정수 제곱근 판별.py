# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    import math
    n = str(math.sqrt(n)).split(".")
    if n[1] != '0':
        return -1
    return pow((int(n[0])+1),2)

n = [
    121,
    3
]

result = [
    144,
    -1
]

for q in [0,1]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')