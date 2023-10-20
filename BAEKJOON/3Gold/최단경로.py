# 그래프 이론, 데이크스트라, 최단 경로
# https://www.acmicpc.net/problem/1753

from collections import defaultdict
input = __import__("sys").stdin.readline

INF = 0xFFFFFFFF
V, E = map(int, input().split())
K = int(input())

graph = defaultdict(list)

for _ in range(E):
    n1,n2,dist = map(int, input().split())
    graph[n1].append((n2,dist))

def dijkstra(start):
    import heapq
    # (비용, 정점) 을 큐에 추가
    queue = [(0, start)]
    visited = [False] * (V+1)
    distance = [INF] * (V+1)
    distance[0] = None
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if visited[node] is True: continue
        visited[node] = True

        # 저장된 거리보다 크면 넘기기
        if distance[node] < dist: continue

        for nxt, cost in graph[node]:
            # _cost = start에서 node까지의 비용 + node에서 nxt까지의 비용
            _cost = distance[node]+cost
            if distance[nxt] < _cost: continue
            distance[nxt] = _cost
            heapq.heappush(queue, (distance[nxt], nxt))
    
    del distance[0]
    return distance

dist = dijkstra(K)
res = ""
for d in dist:
    if d == INF:
        res += "INF\n"
    else:
        res += f"{d}\n"

print(res)