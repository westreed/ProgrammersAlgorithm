# 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색
# https://www.acmicpc.net/problem/1967

import sys, heapq
from collections import defaultdict

INF = 0xFFFFFFFF

def dijkstra(N, graph, start):
    distance = [INF] * (N+1)
    heap = [(0, start)]
    distance[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)

        if distance[node] < cost: continue

        for next_node, next_cost in graph[node]:
            sum_cost = distance[node] + next_cost

            if distance[next_node] < sum_cost: continue
            distance[next_node] = sum_cost
            heapq.heappush(heap, (sum_cost, next_node))
    
    return distance


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    graph = defaultdict(list)

    for _ in range(N-1):
        parent,child,dist = map(int, input().split())
        graph[parent].append((child, dist))
        graph[child].append((parent, dist))
    
    node, dist = 0, 0
    for _node, _dist in enumerate(dijkstra(N, graph, 1)):
        if _dist == INF: continue
        if dist < _dist:
            node = _node
            dist = _dist
    
    dist = 0
    for _node, _dist in enumerate(dijkstra(N, graph, node)):
        if _dist == INF: continue
        if dist < _dist:
            dist = _dist

    print(dist)