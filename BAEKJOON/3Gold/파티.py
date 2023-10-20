# 그래프 이론, 데이크스트라, 최단 경로
# https://www.acmicpc.net/problem/1238

# N 학생의 수 (자기번호가 자기가 살고 있는 마을위치)
# M 단방향 도로 (길)
# X 모여야하는 파티 위치

input = __import__("sys").stdin.readline
from collections import defaultdict
N,M,X = map(int, input().split())
INF = 1e9

Graph = defaultdict(list)
for _ in range(M):
    n1,n2,dist = map(int, input().split())
    Graph[n1].append((n2, dist))

def dijkstra(start):
    import heapq
    # (비용, 정점) 을 큐에 추가
    queue = [(0, start)]
    Distance = [INF] * (N+1)
    Distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        # 저장된 거리보다 크면 넘기기
        if Distance[node] < dist: continue

        for nxt, cost in Graph[node]:
            # _cost = start에서 node까지의 비용 + node에서 nxt까지의 비용
            _cost = Distance[node]+cost
            if Distance[nxt] < _cost: continue
            Distance[nxt] = _cost
            heapq.heappush(queue, (Distance[nxt], nxt))
    
    Distance[0] = None
    return Distance

TotalDistance = [None for _ in range(N+1)]

for n in range(1, N+1):
    TotalDistance[n] = dijkstra(n)

LongDistance = 0
for n in range(1, N+1):
    cur_distance = 0
    # n번 -> x번
    cur_distance += TotalDistance[n][X]
    # x번 -> n번
    cur_distance += TotalDistance[X][n]

    LongDistance = max(LongDistance, cur_distance)

print(LongDistance)