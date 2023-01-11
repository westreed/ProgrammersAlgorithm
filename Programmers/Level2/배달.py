# Summer/Winter Coding(~2018)
# https://programmers.co.kr/learn/courses/30/lessons/12978

def solution(N, road, K):
    #탐색을 위해 필요한 배열 선언
    visit = [0 for _ in range(N)]
    visit[0] = 1
    nodes = [[[] for _ in range(N)] for _ in range(N)]
    
    #road 데이터를 활용하기 쉬운 이중배열로 치환
    for r in road:
        x,y = r[0]-1,r[1]-1
        nodes[x][y].append(r[2])
        nodes[y][x].append(r[2])
    
    #탐색함수
    def dfs(N, nodes, K, visit, value, vill):
        for n in range(N):
            if nodes[vill][n]:
                for r in nodes[vill][n]:
                    if visit[n] == 0 or visit[n] > value+r:
                        visit[n] = value+r
                        dfs(N, nodes, K, visit, value+r, n)
                        
    
    dfs(N, nodes, K, visit, 0, 0)
    
    answer = 0
    for v in visit:
        if v <= K: answer += 1
    return answer

N = [
    5,
    6
]

road = [
    [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],
    [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
]

K = [
    3,
    4
]

result = [
    4,
    4
]

for q in [0,1]:
    qid = solution(N[q], road[q], K[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')