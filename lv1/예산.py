# Summer/Winter Coding (~2018)
# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    answer,cost = 0,0
    for i in d:
        cost += i
        if(cost <= budget):
            answer += 1
            continue
        break
    return answer

d = [
    [1,3,2,5,4],
    [2,2,3,3]
]

budget = [
    9,
    10
]

result = [
    3,
    4
]

for q in [0,1]:
    qid = solution(d[q], budget[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')