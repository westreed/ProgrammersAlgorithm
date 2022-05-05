# 그리디 알고리즘, 정렬
# https://www.acmicpc.net/problem/1931

import sys
from collections import deque
input=sys.stdin.readline

Number = int(input())
Timer  = 0
Confer = []

for _ in range(Number):
    Meet = list(map(int, input().split()))
    Meet.extend([Meet[1]-Meet[0]])
    Confer.append(Meet)

Confer.sort()
Confer = deque(Confer)

print(Confer)

while len(Confer) > 1:
    Meet1 = Confer.popleft()
    Meet2 = Confer.popleft()

    if Meet1[2]