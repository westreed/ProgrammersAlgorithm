# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    n = list(map(int, str(n)))
    n.reverse()
    return n

n = [
    12345
]
result = [
    [5,4,3,2,1]
]

for q in [0]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')