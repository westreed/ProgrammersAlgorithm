# 그래프 이론, 최단 경로, 데이크스트라
# https://www.acmicpc.net/problem/17835

"""
6 10 2
2 6 2
1 4 1
6 1 5
2 5 1
5 1 4
4 5 6
6 2 3
3 5 1
3 1 1
5 2 2
1 2
"""

input = __import__("sys").stdin.readline
N,M,K = map(int, input().split()) # 도시, 도로, 면접장
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[b].append((a,c))

hires = set(map(int, input().split()))
INF = int(1e11)

def dijkstra(starts):
    import heapq

    global far_city, far_cost

    dist = [INF] * (N+1)
    heap = []
    for start in starts:
        heapq.heappush(heap, (0, start))
        dist[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)

        if dist[node] < cost: continue

        for nxt_node, nxt_cost in graph[node]:
            sum_cost = dist[node] + nxt_cost

            if sum_cost >= dist[nxt_node]:
                continue

            dist[nxt_node] = sum_cost
            heapq.heappush(heap, (sum_cost, nxt_node))
    
    return dist


dist = dijkstra(hires)

far_city = N+1
far_cost = 0

for city in range(1, N+1):
    if city in hires:
        continue
    if far_cost < dist[city] and dist[city] != INF:
        far_city = city
        far_cost = dist[city]

print(f"{far_city}\n{far_cost}")