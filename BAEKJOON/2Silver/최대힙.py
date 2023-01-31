# 자료 구조, 우선순위 큐
# https://www.acmicpc.net/problem/11279

import heapq
input = __import__('sys').stdin.readline
N = int(input())

Heap = []
for _ in range(N):
    C = int(input())
    if C == 0:
        if Heap: print(-heapq.heappop(Heap))
        else:    print(0)
        continue
    heapq.heappush(Heap, -C)