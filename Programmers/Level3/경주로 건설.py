# 2020 카카오 인턴십
# https://school.programmers.co.kr/learn/courses/30/lessons/67259

def solution(board):
    from collections import deque
    SIZE = len(board)
    COST = [[[0 if board[y][x] else 0xFFFFFFFF for _ in range(2)] for x in range(SIZE)] for y in range(SIZE)]
    LAST = 0xFFFFFFFF

    Queue = deque()
    # (위치x,y), 비용 이전 방향(0:row, 1:col)
    Queue.append((0,0,0,0))
    Queue.append((0,0,0,1))
    while Queue:
        cx,cy,cost,arrow = Queue.pop()
        if cx == SIZE-1 and cy == SIZE-1:
            LAST = cost
            continue

        for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
            nx, ny = cx+dx, cy+dy
            nArrow = 1 if abs(dx) == 1 else 0
            nCost = cost+100 if nArrow == arrow else cost+600
            if nCost > LAST: continue
            if 0 <= nx < SIZE and 0 <= ny < SIZE and COST[ny][nx][nArrow] >= nCost:
                COST[ny][nx][nArrow] = nCost
                Queue.append((nx, ny, nCost, nArrow))

    return min(COST[SIZE-1][SIZE-1])


board = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],
    [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],
    [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]],
    [[0 for _ in range(25)] for _ in range(25)]
]

result = [
    900,
    3800,
    2100,
    3200,
    5300
]

for q in [0,1,2,3,4]:
    qid = solution(board[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')

# 6*100 + 500*4 = 2600
# 3100?
