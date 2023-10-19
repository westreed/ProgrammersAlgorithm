INF = int(1e9)
N = 6
Graph = {0:[(1,3), (2,2), (3,5)], 1:[(2,2), (4,8)], 2:[(3,2)], 3:[(4,6)], 4:[(5,1)], 5:[]}
Dist = [INF] * N

def dijkstra(start):
    import heapq
    # (비용, 정점) 을 큐에 추가
    queue = [(0, start)]
    Dist[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        # 저장된 거리보다 크면 넘기기
        if Dist[node] < dist: continue

        for nxt, cost in Graph[node]:
            # _cost = start에서 node까지의 비용 + node에서 nxt까지의 비용
            _cost = Dist[node]+cost
            if Dist[nxt] <= _cost: continue
            Dist[nxt] = _cost
            heapq.heappush(queue, (Dist[nxt], nxt))

dijkstra(0)
print(Dist)