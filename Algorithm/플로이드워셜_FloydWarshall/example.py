INF = 0xFFFFFFFF

def Floyd_Warshall(N, Graph):
    dist = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            dist[i][j] = Graph[i][j]
    
    for k in range(N): # 중간 지점
        for i in range(N): # 시작 지점
            for j in range(N): # 도착 지점
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


if __name__ == "__main__":
    N = 4
    Graph = [
        [0, 2, INF, 4],
        [2, 0, INF, 5],
        [3, INF, 0, INF],
        [INF, 2, 1, 0]
    ]

    res = Floyd_Warshall(N, Graph)
    print(res)