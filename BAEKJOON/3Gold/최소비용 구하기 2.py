# 그래프 이론, 데이크스트라, 최단 경로
# https://www.acmicpc.net/problem/11779

INF = float('inf')

def dijkstra(N, graph, start):
    import heapq
    dist = [INF]*(N+1)
    visit = [None]*(N+1)
    dist[start] = 0
    visit[start] = [start]
    heap = [(0,start)]

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]: continue

        for _node, _cost in graph[node]:
            next_cost = _cost + dist[node]
            if next_cost >= dist[_node]: continue
            dist[_node] = next_cost
            visit[_node] = visit[node] + [_node]
            heapq.heappush(heap, (next_cost, _node))
    
    return dist, visit

if __name__ == "__main__":
    input = __import__("sys").stdin.readline
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s,e,c = map(int, input().split())
        graph[s].append((e,c))
    start, end = map(int, input().split())

    dist, visit = dijkstra(N,graph,start)
    print(dist[end])
    print(len(visit[end]))
    print(*visit[end])
