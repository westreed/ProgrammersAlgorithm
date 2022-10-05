# 힙(Heap)
# https://programmers.co.kr/learn/courses/30/lessons/42627


def solution(jobs):
    from heapq import heappop, heappush
    
    jobs.sort()
    Length = len(jobs)
    Answer = 0
    wkTime = 0
    Waiter = []
    heappush(Waiter, (0, jobs.pop(0)))

    while Waiter:
        print(wkTime,Waiter)
        sch = heappop(Waiter)[1]
        if wkTime < sch[0]: wkTime = sch[0]+sch[1]
        else: wkTime += sch[1]
        Answer += (wkTime - sch[0])
        
        while jobs:
            # 현재 처리한 작업 도중에 들어온 작업이 있는 경우
            if wkTime > jobs[0][0]:
                heappush(Waiter, (jobs[0][1], jobs[0]))
                jobs.pop(0)
            # 들어온 작업이 없는 경우
            else:
                if len(Waiter) == 0:
                    time = jobs[0][0]
                    while jobs:
                        if time != jobs[0][0]: break
                        heappush(Waiter, (jobs[0][1], jobs[0]))
                        jobs.pop(0)
                break

    return Answer//Length
            


# 3번의 경우
# 


jobs = [
    [[0, 3], [1, 9], [2, 6]],
    [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]],
    [[0, 20], [1, 5], [2, 1]],
    [[0, 5], [2, 10], [10000, 2]]
]

result = [
    9,
    72,
    12,
    6
]

for q in [0,1,2,3]:
    qid = solution(jobs[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')