# 정렬
# https://www.acmicpc.net/problem/2751

import sys, heapq
input = sys.stdin.readline

N = int(input())
lists = []
for _ in range(N):
    heapq.heappush(lists, int(input()))
for _ in range(N):
    print(heapq.heappop(lists))