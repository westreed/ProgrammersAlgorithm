# 2022 KAKAO TECH INTERNSHIP
# https://school.programmers.co.kr/learn/courses/30/lessons/118669


def solution(n, paths, gates, summits):
    from collections import defaultdict
    INF = int(1e9)

    path = defaultdict(list)
    for i,j,t in paths:
        path[i].append((j,t))
        path[j].append((i,t))

    result = []

    def get_smallest_node(visit, nodes):
        min_value = INF
        index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
        for i in range(1, n + 1):
            if not visit[i] and nodes[i] < min_value:
                min_value = nodes[i]
                index = i
        return index

    for gate in gates:
        visit = [False for _ in range(n+1)]
        nodes = [INF for _ in range(n+1)]
        inten = [0 for _ in range(n+1)]

        nodes[gate] = 0
        visit[gate] = True

        for j,t in path[gate]:
            nodes[j] = t
            inten[j] = t

        for _ in range(n-1):
            now = get_smallest_node(visit, nodes)
            visit[now] = True

            for j,t in path[now]:
                cost = nodes[now] + t
                if cost < nodes[j]:
                    nodes[j] = cost
                    inten[j] = t if inten[now] < t else inten[now]
        
        # print(gate, nodes)
        for s in summits:
            result.append((gate, s, inten[s]))
    
    print(result)
    
    
    

n = [
    6,7,7,5
]
paths = [
    [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
    [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
    [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
    [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]
]
gates = [
    [1, 3],
    [1],
    [3, 7],
    [1, 2]
]
summits = [
    [5],
    [2, 3, 4],
    [1, 5],
    [5]
]

result = [
    [5, 3],
    [3, 4],
    [5, 1],
    [5, 6]
]

for q in [0,1,2,3]:
    qid = solution(n[q], paths[q], gates[q], summits[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')