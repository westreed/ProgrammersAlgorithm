# 2022 KAKAO TECH INTERNSHIP
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    from collections import deque

    count = 0
    length = len(queue1+queue2)*2
    queue = (deque(queue1), deque(queue2))
    queue_sum = [sum(queue1), sum(queue2)]
    target = (queue_sum[0]+queue_sum[1])//2

    # 가장 최소의 이동으로 같게 만들기
    while True:
        if length < count: return -1
        if target == queue_sum[0]: return count
        if target < queue_sum[0]:
            item = queue[0].popleft()
            queue[1].append(item)
            queue_sum[0] -= item
            queue_sum[1] += item
            count += 1

        elif target < queue_sum[1]:
            item = queue[1].popleft()
            queue[0].append(item)
            queue_sum[0] += item
            queue_sum[1] -= item
            count += 1

queue1 = [
    [3, 2, 7, 2],
    [1, 2, 1, 2],
    [1, 1]
]

queue2 = [
    [4, 6, 5, 1],
    [1, 10, 1, 2],
    [1,5]
]

result = [
    2,
    7,
    -1
]

for q in [0,1,2]:
    qid = solution(queue1[q], queue2[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')