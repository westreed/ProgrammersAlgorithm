# 2019 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages): #N은 스테이지갯수
    import operator
    answer = {i+1:0 for i in range(N)}
    for s in range(N):
        failU = stages.count(s+1)
        passU = list(map(lambda x:x>s, stages)).count(True)
        if failU == 0: answer[s+1] = 0
        else: answer[s+1] = -failU/passU
    return list(map(lambda x:x[0], sorted(answer.items(), key=operator.itemgetter(1,0))))

N = [
    5,
    4
]

stages = [
    [2, 1, 2, 6, 2, 4, 3, 3],
    [4,4,4,4,4]
]

result = [
    [3,4,2,1,5],
    [4,1,2,3]
]

for q in [0,1]:
    qid = solution(N[q], stages[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')