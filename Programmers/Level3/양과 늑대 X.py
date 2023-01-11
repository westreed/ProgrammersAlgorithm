# 2022 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/92343

def solution(info, edges):
    Graph = [[] for _ in range(len(info))]
    for i,j in edges:
        Graph[i].append(j)
        Graph[j].append(i)
    
    print(Graph)

info = [
    [0,0,1,1,1,0,1,0,1,0,1,1],
    [0,1,0,1,1,0,1,0,0,1,0]
]

edges = [
    [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]],
    [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
]

result = [5,5]

for q in [0,1]:
    qid = solution(info[q], edges[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')