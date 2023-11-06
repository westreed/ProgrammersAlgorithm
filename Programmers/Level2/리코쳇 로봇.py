# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/169199

def solution(board:list):
    start = None
    goal  = None
    SIZEX = len(board[0])+2
    SIZEY = len(board)+2
    board.insert(0, 'D'*SIZEX)
    board.append('D'*SIZEX)
    for y in range(1,SIZEY-1):
        board[y] = 'D' + board[y] + 'D'

    for y in range(SIZEY):
        for x in range(SIZEX):
            if board[y][x] == 'R':
                start = (x, y)
            elif board[y][x] == 'G':
                goal = (x, y)
                if  0 < x < SIZEX and \
                    0 < y < SIZEY and \
                    board[y-1][x] != 'D' and \
                    board[y+1][x] != 'D' and \
                    board[y][x-1] != 'D' and \
                    board[y][x+1] != 'D':
                    return -1

    # 한쪽이 막혀있으면 해당방향은 제외해야 하고,
    # 이전에 실행했던 방향 역시 제외해야한다.

    def bfs(startPos, goalPos):
        from collections import deque
        # DebugText = ['위', '아래', '왼쪽', '오른쪽']
        Arrow = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        SkipA = {-1:-1, 0:0, 1:0, 2:1, 3:1}
        Queue = deque()
        # 현재위치, 움직인방향, 행동횟수
        Queue.append((startPos, -1, 0))
        while Queue:
            pos,aro,cnt = Queue.popleft()
            if pos == goalPos:
                return cnt
            
            for d, arr in enumerate(Arrow):
                if aro == d: continue
                if SkipA[aro] == SkipA[d]: continue

                _nx, _ny = pos
                ax, ay = arr
                nx, ny = _nx + ax, _ny + ay
                while board[ny][nx] != 'D':
                    _nx, _ny = nx, ny
                    nx, ny = _nx + ax, _ny + ay
                if (_nx, _ny) == pos: continue
                Queue.append(((_nx,_ny), d, cnt+1))
        return -1
    return bfs(start, goal)


board = [
    ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."],
    [".D.R", "....", ".G..", "...D"]
]

result = [7, -1]

for q in [0, 1]:
    qid = solution(board[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')