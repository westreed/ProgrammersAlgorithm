# 그래프 이론, 최단 경로, 데이크스트라
# https://www.acmicpc.net/problem/24042

"""
4 5
1 2
3 4
1 3
4 1
2 3
"""

input = __import__("sys").stdin.readline

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append((b,i))
    graph[b].append((a,i))

INF = int(1e11)

def dijkstra():
    import heapq

    dist = [INF]*(N+1)
    heap = [(0, 1)]
    dist[1] = 0

    while heap:
        cost, node = heapq.heappop(heap)

        if dist[node] < cost:
            continue

        timing = cost % M
        for nxt_node, nxt_timing in graph[node]:
            nxt_cost = dist[node]+1
            if nxt_timing >= timing:
                nxt_cost += nxt_timing-timing
            else:
                nxt_cost += M+nxt_timing-timing

            if nxt_cost >= dist[nxt_node]:
                continue
            
            dist[nxt_node] = nxt_cost
            heapq.heappush(heap, (nxt_cost, nxt_node))

    print(dist[N])

dijkstra()