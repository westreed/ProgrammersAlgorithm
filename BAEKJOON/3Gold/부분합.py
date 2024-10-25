# 누적합, 투 포인터
# https://www.acmicpc.net/problem/1806

import sys

input = sys.stdin.readline
N,M = map(int, input().split())
lists = list(map(int, input().split()))
answer = N+1

start,end = 0,0
sums = lists[0]

while end < N:
    if sums < M:
        end += 1
        if end == N:
            break
        sums += lists[end]
    else:
        l = end-start+1
        answer = min(answer, l)
        sums -= lists[start]
        start += 1

print(answer if answer < N+1 else 0)