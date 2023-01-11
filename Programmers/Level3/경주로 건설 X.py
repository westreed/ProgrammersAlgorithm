# 2020 카카오 인턴십
# https://school.programmers.co.kr/learn/courses/30/lessons/67259

def solution(board):
    import copy
    from collections import deque
    SIZE = len(board)
    RESULT = []


    queue = deque()
    queue.append((0,0,copy.deepcopy(board)))
    while queue:
        cx,cy,map = queue.popleft()
        if cx == SIZE-1 and cy == SIZE-1:
            RESULT.append(map)
            continue
        # 이상태에서 우,하 방향으로만 진행하되 우,하가 막혔을 때 이전방향을 제외한 좌,상 방향 둘 중 하나를 선택하게 하기
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx,ny = cx+dx,cy+dy
            if nx >= 0 and nx < SIZE and ny >= 0 and ny < SIZE:
                if map[ny][nx] == 0:
                    map_ = copy.deepcopy(map)
                    map_[ny][nx] = map_[cy][cx]-1
                    queue.append((nx,ny,map_))

    print(len(RESULT))
    for re in RESULT:
        for r in re:
            print(r)
        print('다음')

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
    0
]

for q in [4]:
    qid = solution(board[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')