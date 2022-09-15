# 2020 카카오 인턴십
# https://school.programmers.co.kr/learn/courses/30/lessons/67259

def solution(board):
    from collections import deque
    SIZE = len(board)

    queue = deque()
    queue.append((0,0))
    while queue:
        cx,cy = queue.popleft()
        if cx == SIZE-1 and cy == SIZE-1: break

        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = cx+dx,cy+dy
            if board[ny][nx] == 0:
                board[ny][nx] = board[cy][cx]-1
                queue.append([nx,ny])

    for b in board:
        print(b)

board = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],
    [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],
    [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
]

result = [
    900,
    3800,
    2100,
    3200
]

for q in [3]:
    qid = solution(board[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')