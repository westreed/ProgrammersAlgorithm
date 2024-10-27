# 자료 구조, 정렬, 우선순위 큐, 투 포인터
# https://www.acmicpc.net/problem/2461

import sys
import heapq

input = sys.stdin.readline
N,M = map(int, input().split())
classes = [list(map(int, input().split())) for _ in range(N)]
for n in range(N):
    heapq.heapify(classes[n])

if N == 1:
    print(0)
    exit(0)

INF = int(1e9)
answer = INF
mins = INF
maxs = 0
participants = []
for n in range(N):
    val = heapq.heappop(classes[n])
    maxs = max(maxs, val)
    mins = min(mins, val)
    heapq.heappush(participants, (val, n))

mins_flag = True
while True:
    if mins_flag:
        mins = max(mins, participants[0][0])

    diff = maxs-mins
    answer = min(answer, diff)

    min_idx = None
    while participants:
        _, min_idx = heapq.heappop(participants)
        if classes[min_idx]:
            break
        else:
            mins_flag = False
    else:
        break
    
    new_val = heapq.heappop(classes[min_idx])
    maxs = max(maxs, new_val)
    heapq.heappush(participants, (new_val, min_idx))

print(answer)