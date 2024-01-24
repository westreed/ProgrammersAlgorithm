# 그래프 이론, 최단 경로, 플로이드-워셜
# https://www.acmicpc.net/problem/11404

INF = 0xFFFFFFFF

def Floyd_Warshall(N, Graph):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                Graph[i][j] = min(Graph[i][j], Graph[i][k] + Graph[k][j])

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    M = int(input())
    Graph = [[0 if i == j else INF for j in range(N)] for i in range(N)]

    for _ in range(M):
        i,j,d = map(int, input().split())
        Graph[i-1][j-1] = min(Graph[i-1][j-1], d)
    
    Floyd_Warshall(N, Graph)
    for g in Graph:
        for node in g:
            print(f"{node if node != INF else 0}", end=" ")
        print()