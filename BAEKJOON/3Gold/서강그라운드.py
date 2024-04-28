# 그래프 이론, 데이크스트라, 최단 경로, 플로이드–워셜
# https://www.acmicpc.net/problem/14938

# 두 지역 간에 더 짧은 경로가 있을 수 있음.
# 

def dijkstra(items, graph, M, start):
    import heapq
    
    INF = 0xFFFFFFFF
    dist = [INF for _ in range(N+1)]
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]: continue

        for _node, _cost in graph[node]:
            sum_cost = dist[node] + _cost
            if sum_cost >= dist[_node]: continue
            if sum_cost > M: continue
            dist[_node] = sum_cost
            heapq.heappush(heap, (sum_cost, _node))
    
    total_item = 0
    for i in range(1, N+1):
        if dist[i] != INF:
            total_item += items[i]
    return total_item

if __name__ == "__main__":
    from collections import defaultdict
    input = __import__("sys").stdin.readline

    N,M,R = map(int, input().split())
    items = [None] + list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(R):
        a,b,l = map(int, input().split())
        graph[a].append((b,l))
        graph[b].append((a,l))
    
    max_item = 0
    for n in range(1, N+1):
        item = dijkstra(items, graph, M, n)
        if max_item < item:
            max_item = item
    
    print(max_item)