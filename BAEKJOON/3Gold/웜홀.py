# 그래프 이론, 최단 경로, 벨만-포드
# https://www.acmicpc.net/problem/1865

import sys

input = sys.stdin.readline
TC = int(input())

def bellmanFord(graph, n, start):
    INF = sys.maxsize
    dist = [INF] * (n+1)
    dist[start] = 0

    for i in range(n):
        for s in range(1, n+1):
            for e, t in graph[s]:
                if dist[e] > dist[s] + t:
                    dist[e] = dist[s] + t
                    if i == n-1:
                        # 마지막 반복에서도 최단거리가 갱신되면 음수 순환이 존재
                        return True
    return False

for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    start = None

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E,T))
        graph[E].append((S,T))
        if start is None:
            # 도로는 양방향이므로 반드시 어딘가와 연결되어 있음.
            start = S
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E,-T))
    
    if bellmanFord(graph, N, start):
        print("YES")
    else:
        print("NO")
