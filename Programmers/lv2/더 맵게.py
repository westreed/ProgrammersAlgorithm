# 힙(Heap)
# https://programmers.co.kr/learn/courses/30/lessons/42626

def solution(scoville, K):
    from heapq import heapify, heappop, heappush
    
    answer = 0
    length = len(scoville)
    heapify(scoville)
    while(True):
        minS = heappop(scoville) #가장 작은 첫번째원소 pop
        if(minS < K):
            if(length > 1):
                minS2 = heappop(scoville) #두번째로 작은 원소 pop
                newScoville = minS + minS2*2
                heappush(scoville,newScoville)
                length -= 1
                answer += 1
                continue
            return -1
        return answer

scoville = [
    [1, 2, 3, 9, 10, 12]
]

K = [7]

result = [2]

for q in [0]:
    qid = solution(scoville[q], K[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')