# 월간 코드 챌린지 시즌2
# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if(signs[i] == True):
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

absolutes = [
    [4,7,12],
    [1,2,3]
]

signs = [
    [True, False, True],
    [False, False, True]
]

result = [
    9,
    0
]

for q in [0,1]:
    qid = solution(absolutes[q], signs[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')