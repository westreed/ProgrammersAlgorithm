

def topologySort(graph):
    from collections import deque
    queue = deque()
    degree = [0] * len(graph)

    # 진입차수 계산하기
    for n in range(len(graph)):
        for i in graph[n]:
            degree[i] += 1

    # 진입차수가 0인 노드 추가하기
    for n in range(len(graph)):
        if degree[n] == 0:
            queue.append(n)
    
    for n in range(len(graph)):
        if not queue:
            print("사이클이 존재합니다.")
            return False
        
        node = queue.pop()
        print(node, end=" ")
        
        for next in graph[node]:
            degree[next] -= 1
            if degree[next] == 0:
                queue.append(next)
    
    return True

if __name__ == "__main__":
    N = 7
    graph = [[] for _ in range(N)]
    degree = [0 for _ in range(N)]

    graph[0].append(1)
    graph[1].append(2)
    graph[2].append(3)
    graph[0].append(4)
    graph[4].append(5)
    graph[3].append(5)
    graph[5].append(6)

    topologySort(graph)