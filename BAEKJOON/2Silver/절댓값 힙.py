# 자료 구조, 우선순위 큐
# https://www.acmicpc.net/problem/11286

input = __import__("sys").stdin.readline
N = int(input())

import heapq
heap = []
for i in range(N):
    val = int(input())
    if val == 0:
        if heap: print(heapq.heappop(heap)[1])
        else: print(0)
    else: heapq.heappush(heap, (abs(val), val))