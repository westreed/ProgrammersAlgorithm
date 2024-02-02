# 그래프 이론, 그래프 탐색, 트리, 너비 우선 탐색, 깊이 우선 탐색
# https://www.acmicpc.net/problem/11725

def find_parent(graph, parents):
    from collections import deque
    queue = deque([1])
    while queue:
        current = queue.popleft()
        for next_node in graph[current]:
            if parents[next_node] is None:
                parents[next_node] = current
                queue.append(next_node)

if __name__ == "__main__":
    import sys
    from collections import defaultdict
    input = sys.stdin.readline

    N = int(input())
    graph = defaultdict(list)
    parents = [None for _ in range(N+1)]

    for _ in range(N-1):
        a,b = map(int, input().split())
        
        graph[a].append(b)
        graph[b].append(a)
    
    find_parent(graph, parents)
    for node in range(2, N+1):
        print(parents[node])