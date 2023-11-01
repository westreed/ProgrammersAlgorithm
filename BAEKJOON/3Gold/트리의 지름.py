# 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색
# https://www.acmicpc.net/problem/1167

# 트리의 지름 : 임의의 두 점 사이의 거리 중 가장 긴 것

input = __import__("sys").stdin.readline
from collections import defaultdict

V = int(input())
graph = defaultdict(list)
for _ in range(V):
    node, *info, _ = list(map(int, input().split()))
    
    for idx in range(len(info) // 2):
        idx = idx*2
        graph[node-1].append((info[idx]-1, info[idx+1]))

def dijkstra(graph, start):
    import heapq
    INF = 0xFFFFFFFF
    dist = [INF] * V
    heap = [(0, start)]
    dist[start] = 0

    while heap:
        _cost, _node = heapq.heappop(heap)

        if dist[_node] < _cost: continue

        for _next_node, _next_cost in graph[_node]:
            _sum_cost = dist[_node] + _next_cost
            if dist[_next_node] < _sum_cost: continue
            dist[_next_node] = _sum_cost
            heapq.heappush(heap, (_sum_cost, _next_node))

    return dist

_max = (0,0)
res = dijkstra(graph, 0)
for idx in range(V):
    if _max[1] < res[idx]:
        _max = (idx, res[idx])

res2 = dijkstra(graph, _max[0])
print(max(res2))

# 아무 노드에서 출발해서 가장 먼 노드를 고른 후,
# 해당 노드에서 다시 출발해서 가장 먼 노드까지의 거리가 트리의 지름.