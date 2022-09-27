# 수학, 비트마스킹
# https://www.acmicpc.net/problem/1094

'''
23
32
64
48
'''

import heapq
Length = int(input())
Rod = []
heapq.heappush(Rod, 64)

while True:
    if sum(Rod) <= Length: break
    small = heapq.heappop(Rod)
    if small == 1: break
    half = small//2
    heapq.heappush(Rod, half)
    if sum(Rod) >= Length: continue
    heapq.heappush(Rod, half)

print(len(Rod))