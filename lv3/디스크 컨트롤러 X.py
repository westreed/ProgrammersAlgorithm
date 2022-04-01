# 힙(Heap)
# https://programmers.co.kr/learn/courses/30/lessons/42627

class Job:
    def __init__(self, arrive, runtime):
        self.value = arrive+runtime
        self.arrive = arrive
        self.runtime = runtime

    def __lt__(self, other):
        return self.value < other.value
    
    def print(self):
        print(self.value, self.arrive, self.runtime)



def solution(jobs):
    import heapq
    from collections import deque

    length = len(jobs)
    runing = 0 # 소요시간
    workIn = []
    finish = []

    jobList = []
    for i in range(length):
        jobList.append(Job(jobs[i][0], jobs[i][1]))
    
    jobList = sorted(jobList)
    for i in range(length):
        jobList[i].print()

    



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

for q in [0]:
    qid = solution(jobs[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')