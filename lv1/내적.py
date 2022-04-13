# 월간 코드 챌린지 시즌1
# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

a = [
    [1,2,3,4],
    [-1,0,1]
]

b = [
    [-3,-1,0,2],
    [1,0,-1]
]

result = [
    3,
    -2
]


for q in [0,1]:
    qid = solution(a[q], b[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')