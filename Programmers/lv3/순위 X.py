# 그래프
# https://programmers.co.kr/learn/courses/30/lessons/49191

def bfs(Graph, n, start):
    from collections import deque

    queue = deque([start])
    visit = [False for _ in range(n+1)]
    result = []
    while queue:
        node = queue.popleft()
        for next in Graph[node]:
            if visit[next] is False:
                visit[next] = True
                queue.append(next)
                result.append(next)
    
    return result


def solution(n, results):
    from collections import defaultdict

    Graph = defaultdict(list)
    Defeat = [0]
    for t1,t2 in results:
        Graph[t2].append(t1)
    
    for node in range(1,n+1):
        l = bfs(Graph, n, node)
        Defeat.append(l)
    
    print(Defeat)
    pass

    


n = [
    5
]
results = [
    [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]],
    [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]
]
result = [
    2,
    1
]

for q in [0]:
    qid = solution(n[q], results[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')