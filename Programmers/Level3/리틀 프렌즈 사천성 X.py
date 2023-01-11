# 2017 카카오코드 본선
# https://programmers.co.kr/learn/courses/30/lessons/1836

def findPath(start, board):
    from copy import deepcopy
    from collections import deque

    queue = deque()
    queue.append([start, -1, -1, []])

    sx,sy = start
    target = board[sy][sx]
    board[sy][sx] = '*'

    m,n = len(board[0]), len(board)
    
    mx = [0,0,1,-1]
    my = [1,-1,0,0]

    result = []

    while queue:
        pos,direction,corner,path = queue.popleft()
        px,py = pos
        print(pos,direction,corner,path)

        for d in range(4):
            dx = px + mx[d]
            dy = py + my[d]
            if dx < 0 or dy < 0 \
                or dx >= m or dy >= n:
                continue
            if board[dy][dx] == '*':
                continue
            
            _direction = deepcopy(direction)
            _corner = deepcopy(corner)
            if direction == -1:
                _direction = d
            elif direction != d and corner == -1:
                _direction = d
                _corner = 0
            else:
                continue
            
            if board[dy][dx] == target:
                result.append(path)
                break

            board[dy][dx] = '*'
            queue.append([[dx,dy],_direction,_corner,path+[[dx,dy]]])
    
    print(result)


def solution(m, n, board):
    board = list(map(list, board))
    for b in board:
        print(b)
    
    findPath([0,0], board)

m = [
    3,
    2,
    4,
    2,
    4
]

n = [
    3,
    4,
    4,
    2,
    4
]

board = [
    ["DBA", "C*A", "CDB"],
    ["NRYN", "ARYA"],
    [".ZI.", "M.**", "MZU.", ".IU."],
    ["AB", "BA"],
    ["A...", "..B.", "B...", "...A"]
]

result = [
    "ABCD",
    "RYAN",
    "MUZI",
    "IMPOSSIBLE",
    "AB"
]

for q in [4]:
    qid = solution(m[q], n[q], board[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')