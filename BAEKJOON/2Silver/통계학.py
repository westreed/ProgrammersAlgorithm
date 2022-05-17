# 수학, 구현, 정렬
# https://www.acmicpc.net/problem/2108

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
lists = []
count = defaultdict(int)

for _ in range(N):
    n = int(input())
    lists.append(n)
    count[n] += 1

lists.sort()
maxv = max(count.values()) # 최빈값
cntlists = []
for k,v in count.items():
    if v == maxv:
        cntlists.append(k)
cntlists.sort()

print(round(sum(lists)/N))
print(lists[N//2])
print(cntlists[0] if len(cntlists) == 1 else cntlists[1])
print(lists[-1]-lists[0])