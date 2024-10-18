# 그래프 이론, 이분 탐색, 최단 경로, 데이크스트라, 매개 변수 탐색
# https://www.acmicpc.net/problem/20183

"""
5 5 1 3 10
1 2 5
2 3 5
1 4 1
4 5 6
5 3 1
"""

input = __import__("sys").stdin.readline

N,M,A,B,C = map(int, input().split())
graph = [[] for _ in range(N+1)]
costs = []
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    costs.append(c)

costs.sort()

INF = int(1e15)

def dijkstra(limit_cost):
    import heapq

    heap = [(0,A)] # 비용, 노드
    dist = [INF]*(N+1) # 비용
    dist[A] = 0

    while heap:
        cost, node = heapq.heappop(heap)

        if dist[node] < cost:
            continue

        for nxt_node, nxt_cost in graph[node]:
            sum_cost = dist[node] + nxt_cost

            if limit_cost < nxt_cost:
                continue

            if sum_cost > C or dist[nxt_node] <= sum_cost:
                continue

            dist[nxt_node] = sum_cost

            heapq.heappush(heap, (sum_cost, nxt_node))
    
    return dist[B]

l = 0
r = M-1
answer = INF

while l <= r:
    mid = (l+r)//2
    cost = dijkstra(costs[mid])
    if cost == INF:
        l = mid+1
    else:
        r = mid-1
        answer = min(costs[mid], answer)

print(-1 if answer == INF else answer)