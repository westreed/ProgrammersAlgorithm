# 그래프 이론, 데이크스트라, 최단 경로
# https://www.acmicpc.net/problem/1916

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start_node, end_node, cost = map(int, input().split())
    graph[start_node].append((end_node, cost))

S, E = map(int, input().split())
INF = sys.maxsize
dist = [INF for _ in range(N+1)]

def dijkstra(start):
    import heapq
    global graph, dist
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)

        if dist[node] < cost: continue

        for next_node, next_cost in graph[node]:
            next_cost += dist[node]
            
            # 같은 경우도 스킵처리를 해줘야 하는데 안해줘서 메모리 초과 뜸.
            # if dist[next_node] < next_cost: continue
            if dist[next_node] <= next_cost: continue
            dist[next_node] = next_cost
            heapq.heappush(heap, (next_cost, next_node))
    
    return dist

print(dijkstra(S)[E])