# 깊이/너비 우선 탐색(DFS/BFS)
# https://school.programmers.co.kr/learn/courses/30/lessons/84021
def searchPiece(board, start, piece, M):
    from collections import deque
    visit = [start]
    node = deque([start])
    temp = deque()
    arrow = {'L':(-1,0), 'R':(1,0), 'U':(0,-1), 'D':(0,1)}
    record = ''
    step = 0
    dot = True
    #노드값은 좌표+방향으로 저장해야됨 [(0,0)]

    while node:
        x,y = node.popleft()
        for d in ['L', 'R', 'U', 'D']:
            nx,ny = x+arrow[d][0], y+arrow[d][1]
            if 0 <= nx and nx < M and 0 <= ny and ny < M and board[ny][nx] == 1:
                if (nx,ny) not in visit:
                    visit.append((nx,ny))
                    temp.append((nx,ny))
                    record = record + str(step) + d
                    dot = False
        if dot: record = record + str(step) + 'O'
        if not node:
            if not temp: break
            node = temp
            temp = deque()
            step += 1

    for x,y in visit: board[y][x] = 0
    visit = sorted(visit, key= lambda x:(x[0]+x[1]))
    first = visit[0]
    for idx in range(len(visit)):
        node = visit[idx]
        visit[idx] = (node[0]-first[0], node[1]-first[1])
    piece.append(visit)

def solution(game_board, table):
    #보드크기
    M = len(table)
    table_Piece = []

    for y in range(M):
        for x in range(M):
            #게임테이블 반전
            if game_board[y][x] == 1: game_board[y][x] = 0
            else: game_board[y][x] = 1
            
            #테이블 분석
            if table[y][x] == 1:
                searchPiece(table, (x,y), table_Piece, M)
    
    print(table_Piece)
    pass

game_board = [
    [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
    [[0,0,0],[1,1,0],[1,1,1]]
]

table = [
    [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]],
    [[1,1,1],[1,0,0],[0,0,0]]
]

result = [
    14,
    0
]

for q in [0]:
    qid = solution(game_board[q], table[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')