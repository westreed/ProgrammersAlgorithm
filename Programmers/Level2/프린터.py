# 스택/큐
# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    prior = [(index , pri) for index, pri in zip([i for i in range(len(priorities))],priorities)]
    index = 0
    while True:
        state = True
        paper = prior[0]
        del prior[0]
        for p in prior:
            if p[1] > paper[1]:
                prior.append(paper)
                state = False
                break
        if state:
            index += 1
            if paper[0] == location:
                return index
    return 0

priorities = [
    [2, 1, 3, 2],
    [1, 1, 9, 1, 1, 1]
]

location = [
    2,
    0
]

result = [
    1,
    5
]

for q in [0,1]:
    qid = solution(priorities[q], location[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')