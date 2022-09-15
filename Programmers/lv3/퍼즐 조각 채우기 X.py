# 깊이/너비 우선 탐색(DFS/BFS)
# https://school.programmers.co.kr/learn/courses/30/lessons/84021

def searchPiece(board, Size, Check):
    from collections import deque

    Piece = []
    for y in range(Size):
        for x in range(Size):
            if board[y][x] == Check:
                visit = [(x,y)]
                node = deque([(x,y)])
                temp = deque()

                while node:
                    cx,cy = node.popleft()
                    for dx,dy in (-1,0), (1,0), (0,-1), (0,1):
                        nx,ny = cx+dx, cy+dy
                        if 0 <= nx and nx < Size and 0 <= ny and ny < Size and board[ny][nx] == Check:
                            if (nx,ny) not in visit:
                                visit.append((nx,ny))
                                temp.append((nx,ny))
                    if not node:
                        if not temp: break
                        node = temp
                        temp = deque()

                for vx,vy in visit: board[vy][vx] = not Check
                visit = sorted(visit, key= lambda x:(x[0]+x[1]))
                first = visit[0]
                for idx in range(len(visit)):
                    visit[idx] = (visit[idx][0]-first[0], visit[idx][1]-first[1])
                Piece.append(visit)
    return Piece

def solution(game_board, table):
    #보드크기
    Size = len(table)
    table_Piece = searchPiece(table, Size, 1)
    blank_Piece = searchPiece(game_board, Size, 0)
    
    print(table_Piece)
    print(blank_Piece)

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