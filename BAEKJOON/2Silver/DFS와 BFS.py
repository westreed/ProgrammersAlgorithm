# BFS, DFS
# https://www.acmicpc.net/problem/1260

from collections import defaultdict

N,M,V = map(int, input().split())
Graph = defaultdict(list)
for _ in range(M):
    node1, node2 = map(int, input().split())
    Graph[node1].append(node2)
    Graph[node2].append(node1)

for k in Graph:
    Graph[k].sort()

def bfs(v, n, graph):
    from collections import deque

    queue = deque([v])
    visit = [False for _ in range(n+1)]
    visit[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for k in graph[node]:
            if visit[k] is False:
                queue.append(k)
                visit[k] = True

def dfs(node, visit, graph):
    print(node, end=' ')
    visit[node] = True
    for k in graph[node]:
        if visit[k] is False:
            dfs(k, visit, graph)

dfs(V, [False for _ in range(N+1)], Graph)
print()
bfs(V, N, Graph)