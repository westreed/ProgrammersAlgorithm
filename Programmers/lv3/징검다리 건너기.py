# 2019 카카오 개발자 겨울 인턴십
# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    MIN = min(stones)
    if k > len(stones): k = len(stones)
    VAL = k if k > MIN else MIN
    print(VAL)

    while True:
        CNT = 0
        for value in stones:
            if value > VAL: CNT = 0
            else:
                CNT += 1
                if CNT >= k:
                    return VAL
        VAL += 1

stones = [
    [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
]

k = [
    11
]

result = [
    3
]

for q in [0]:
    qid = solution(stones[q], k[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')