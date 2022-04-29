# 자료 구조, 문자열, 정렬, 해시를 사용한 집합과 맵
# https://www.acmicpc.net/problem/1764

import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
humans  = defaultdict(int)
hearsay = []
for _ in range(N): humans[input().strip()] = 1
for _ in range(M):
    name = input().strip()
    if humans.get(name): heapq.heappush(hearsay, name)

print(len(hearsay))
answer = ''
while hearsay:
    answer += heapq.heappop(hearsay)+'\n'
print(answer)
