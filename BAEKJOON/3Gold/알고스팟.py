# 그래프 이론, 그래프 탐색, 최단 경로, 데이크스트라, 0-1 너비 우선 탐색
# https://www.acmicpc.net/problem/1261

input = __import__("sys").stdin.readline
M,N = map(int, input().split())
board = [input() for _ in range(N)]


def dijkstra(start: tuple):
    import heapq

    INF = 0xFFFFFFFF
    distance = [[INF for _ in range(M)] for _ in range(N)]

    # (비용, 정점) 을 큐에 추가
    queue = [(0, start)]
    x,y = start
    distance[x][y] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        cx, cy = node

        # 저장된 거리보다 크면 넘기기
        if distance[cx][cy] < dist: continue

        # 연결된 간선 중에서 비용이 낮은 경로 등록하기
        arrow = ((-1,0),(1,0),(0,-1),(0,1))
        for dx, dy in arrow:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx >= N: continue
            if ny < 0 or ny >= M: continue

            cost = int(board[nx][ny])
            _cost = distance[cx][cy] + cost
            if distance[nx][ny] <= _cost: continue

            distance[nx][ny] = _cost
            heapq.heappush(queue, (_cost, (nx, ny)))
    
    return distance[N-1][M-1]
    

print(dijkstra((0,0)))