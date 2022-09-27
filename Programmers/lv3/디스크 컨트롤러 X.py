# 힙(Heap)
# https://programmers.co.kr/learn/courses/30/lessons/42627


def solution(jobs):
    import heapq
    from collections import deque

    length = len(jobs)
    runing = 0 # 소요시간
    heapq1 = []
    heapq2 = []
    for idx,job in enumerate(jobs):
        heapq.heappush(heapq1, (job[1],idx))
        heapq.heappush(heapq2, (job[0]+job[1],idx))
    
    for j in range(len(jobs)):
        t1 = heapq.heappop(heapq1)
        t2 = heapq.heappop(heapq2)
        print(t1,t2)
    



jobs = [
    [[0, 3], [1, 9], [2, 6]],
    [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]],
    [[0, 20], [1, 5], [2, 1]]
]

result = [
    9,
    72,
    12
]

for q in [2]:
    qid = solution(jobs[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')