# 위클리 챌린지
# https://programmers.co.kr/learn/courses/30/lessons/86971

def solution(n, wires):
    from collections import deque

    def graph(graph, root):
        visited = []
        queue = deque([root])

        while queue:
            n = queue.popleft()
            if n not in visited:
                visited.append(n)
                if graph.get(n):
                    queue += graph[n] - set(visited)
                else: return len(visited)
        return len(visited)

    answer = 101
    #모든 선을 다 끊어서, 각 경우에 따른 갯수 구하기.
    for w in range(len(wires)):
        wires_ = wires[:]
        cutLine = wires_[w]
        del wires_[w]

        graphNode = {}
        for wi in wires_:
            if graphNode.get(wi[0]): graphNode[wi[0]].add(wi[1])
            else: graphNode[wi[0]] = set([wi[1]])
            if graphNode.get(wi[1]): graphNode[wi[1]].add(wi[0])
            else: graphNode[wi[1]] = set([wi[0]])

        a = graph(graphNode, cutLine[0])
        b = abs((n-a) - a)
        if b < answer: answer = b
    return answer

n = [
    9,
    4,
    7
]

wires = [
    [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]],
    [[1,2],[2,3],[3,4]],
    [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
]

result = [
    3,
    0,
    1
]

for q in [0,1,2]:
    qid = solution(n[q], wires[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')