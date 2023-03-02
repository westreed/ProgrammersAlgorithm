# 
# https://www.acmicpc.net/problem/11403

from collections import defaultdict, deque
input = __import__("sys").stdin.readline
N = int(input())
Graph = defaultdict(set)

for i in range(N):
    node = list(map(int, input().split()))
    for j in range(N):
        if node[j]:
            Graph[i].add(j)

def dfs(start, target):
    queue = deque([(start, 0)])
    visit = set()
    while queue:
        node, cnt = queue.popleft()
        if cnt > 0 and node == target: return True

        for next in Graph[node]:
            if next not in visit:
                visit.add(next)
                queue.append((next, cnt+1))
    return False
    
maps = [[0 for _ in range(N)] for _ in range(N)]
for x in range(N):
    for y in range(N):
        res = dfs(x, y)
        if res: maps[x][y] = 1

for map in maps:
    print(*map)