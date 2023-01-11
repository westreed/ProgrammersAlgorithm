# 이분탐색
# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = max(times)*n
    start = 0
    end = answer
    while start <= end:
        # mid는 통과시간
        mid = (start+end) // 2
        total = 0
        for time in times:
            total += mid // time

        # 통과인원이 너무 적은 경우 (최소값 늘리기)
        if n > total:
            start = mid + 1
        # 통과인원이 너무 많은 경우 (최대값 줄이기)
        else:
            answer = min(answer, mid)
            end = mid - 1
    return answer
    

n = [
    6,
    3,
    3
]
times = [
    [7,10],
    [1,1,1],
    [1,2,3]
]
result = [
    28,
    1,
    2,
]

for q in [0,1,2]:
    qid = solution(n[q], times[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')