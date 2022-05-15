# 정렬
# https://www.acmicpc.net/problem/1015
from collections import defaultdict

N = int(input())
lists = list(map(int, input().split()))
sorted_lists = sorted(lists)
index = defaultdict(int)
answer = []

for cur in lists:
    idx = index.get(cur)
    if not idx:
        idx = 0
    index[cur] += 1
    
    for k,v in enumerate(sorted_lists):
        if cur == v:
            if idx:
                idx -= 1
                continue
            else:
                answer.append(k)
                break

print(*answer)