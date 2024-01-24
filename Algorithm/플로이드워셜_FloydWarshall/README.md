# 플로이드-워셜 (Floyd-Warshall)

다익스트라는 하나의 정점에서 다른 모든 정점까지의 최단 거리를 구하는 알고리즘(S.S.S.P - Single Source Shortest Path) 이었다면, 플로이드-워셜 알고리즘은 한 번 실행하여 모든 노드 간 최단 경로를 구할 수 있다.

또한, 플로이드-워셜 알고리즘은 다익스트라 알고리즘과는 다르게 음의 간선도 사용할 수 있다.

주의해야 할 부분은 시간복잡도가 O(n^3)으로, 그래프의 크기가 작아 세제곱 시간 알고리즘을 적용해도 문제가 풀릴 때만 사용할 수 있다.

```py

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

```