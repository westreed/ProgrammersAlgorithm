# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    num = str(n)
    answer = 0
    for i in range(len(num)):
        answer += int(num[i])
    return answer

N = [
    123,
    987
]

result = [
    6,
    24
]

for q in [0,1]:
    qid = solution(N[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')