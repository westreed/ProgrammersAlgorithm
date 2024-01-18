# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    import itertools
    
    length = len(elements)
    cyc = itertools.cycle(elements)
    
    answer = set([sum(elements)])
    for _ in range(length):
        sums = 0
        for _ in range(length):
            sums += next(cyc)
            answer.add(sums)
        next(cyc)
    
    return len(answer)

elements = [
    [7,9,1,1,4]
]

result = [
    18
]

for q in [0]:
    qid = solution(elements[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')