# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    from collections import defaultdict

    count = defaultdict(int)
    for tan in tangerine:
        count[tan] += 1

    print(count)
    answer = 0
    tangerine_list = dict(sorted(list(count.items()), key=lambda x: -x[1]))
    print(tangerine_list)
    # while k > 0:
    #     _, cnt = tangerine_list.pop(0)
    #     answer += 1
    #     k -= cnt

    return answer

k = [6,4,2]
tangerine = [
    [1, 3, 2, 5, 4, 5, 2, 3],
    [1, 3, 2, 5, 4, 5, 2, 3],
    [1, 1, 1, 1, 2, 2, 2, 3],
]
result = [3,2,1]

for q in [0,1,2]:
    qid = solution(k[q], tangerine[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')