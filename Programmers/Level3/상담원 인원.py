# 2023 현대모비스 알고리즘 경진대회 예선
# https://school.programmers.co.kr/learn/courses/30/lessons/214288

def counseling(mento_list, reqs):
    import heapq
    
    wait = 0
    mento = [[0]*x for x in mento_list]

    for start,end,mtype in reqs:
        time = heapq.heappop(mento[mtype-1])
        wait += max(0, time-start)
        heapq.heappush(mento[mtype-1], max(start, time)+end)

    return wait


def solution(k, n, reqs):
    # k 상담유형
    # n 멘토인원
    # reqs 상담요청
    from itertools import product

    answer = 0xFFFFFFFF
    for mento in product(range(1, n+1), repeat=k):
        if sum(mento) != n:
            continue
        _ans = counseling(mento, reqs)
        if answer > _ans:
            answer = _ans
    
    return answer


k = [3,2]
n = [5,3]
reqs = [
    [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]],
    [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]
]
result = [
    25,
    90
]

for q in [0,1]:
    qid = solution(k[q], n[q], reqs[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')