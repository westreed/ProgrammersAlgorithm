# 그래프 이론, 데이크스트라, 최단 경로
# https://www.acmicpc.net/problem/1504

from collections import defaultdict
input = __import__("sys").stdin.readline

INF = 0xFFFFFFFF
N, E = map(int, input().split())

graph = defaultdict(list)

for _ in range(E):
    n1,n2,dist = map(int, input().split())
    graph[n1].append((n2,dist))
    graph[n2].append((n1,dist))

V1, V2 = map(int, input().split()) # 반드시 들려야하는 정점


def dijkstra(start):
    import heapq
    # (비용, 정점) 을 큐에 추가
    queue = [(0, start)]
    distance = [INF] * (N+1)
    distance[0] = None
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        # 저장된 거리보다 크면 넘기기
        if distance[node] < dist: continue

        for nxt, cost in graph[node]:
            # _cost = start에서 node까지의 비용 + node에서 nxt까지의 비용
            _cost = distance[node]+cost
            if distance[nxt] < _cost: continue
            distance[nxt] = _cost
            heapq.heappush(queue, (distance[nxt], nxt))
    print(distance)
    return distance

def ShortPath():
    # 1번 노드 > V1, V2 > N번 노드
    total = [0, 0]
    dist = dijkstra(1)
    if INF in (dist[V1], dist[V2], dist[N]): return print(-1)

    total[0] += dist[V1]
    total[1] += dist[V2]

    for v1, v2, t1, t2 in [(V1, V2, V2, V1), (V2, V1, N, N)]:
        dist1 = dijkstra(v1)
        dist2 = dijkstra(v2)

        total[0] += dist1[t1]
        total[1] += dist2[t2]

    return print(min(total))
    
ShortPath()