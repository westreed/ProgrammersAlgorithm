# 이분탐색
# https://programmers.co.kr/learn/courses/30/lessons/43236


def solution(distance, rocks, n):
    answer = 0
    rocks = [0] + sorted(rocks) + [distance]
    perDistance = [rocks[i+1]-rocks[i] for i in range(len(rocks)-1)]
    perNumber = len(perDistance)
    print(perDistance)

    for _ in range(n):
        minv = 0
        for d in range(perNumber):
            if perDistance[d] < perDistance[minv]:
                minv = d
        
        value = perDistance[minv]
        del perDistance[minv]
        perNumber -= 1
        if minv == 0:
            perDistance[minv] += value
        elif minv == perNumber:
            perDistance[minv-1] += value
        else:
            perDistance[minv] += value
    
    return min(perDistance)




    # start = 1
    # end = distance
    # while start <= end:
    #     mid = (start+end) // 2

    # return answer


distance = [25]
rocks = [
    [2, 14, 11, 21, 17]
]
n = [2]
result = [4]

for q in [0]:
    qid = solution(distance[q], rocks[q], n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')