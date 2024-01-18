# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/169199

def find_point_pos(board,N,M):
    start, goal = None, None
    for n in range(N):
        for m in range(M):
            if board[n][m] == 'R':
                start = (n,m)
            elif board[n][m] == 'G':
                goal = (n,m)
            if start is not None\
                and goal is not None:
                return start, goal

def bfs(board,N,M,start,goal):
    from collections import deque

    visit = [[0] * M for _ in range(N)]
    print(visit)
    queue = deque()
    queue.append((start, -1, 0))
    # U1 D2 L4 R8
    arrow = ((0, -1, 0), (1, 1, 0), (2, 0, -1), (3, 0, 1))
    reverse = (0, 0, 1, 1, -1)

    while queue:
        pos, d, cnt = queue.popleft()

        if pos == goal:
            for b in board:
                print(b)
            for v in visit:
                print(v)
            return cnt
        
        for _d, dx, dy in arrow:
            nx,ny = pos
            if reverse[_d] == reverse[d]: continue

            while True:
                _nx,_ny = nx+dx, ny+dy
                if 0 > _nx or _nx >= N: break
                if 0 > _ny or _ny >= M: break
                if board[_nx][_ny] == "D": break
                nx,ny = _nx,_ny
            
            if visit[nx][ny] & (1 << _d): continue
            visit[nx][ny] += 1 << _d
            queue.append(((nx,ny), _d, cnt+1))
    
    return -1



def solution(board):
    N,M = len(board), len(board[0])
    start, goal = find_point_pos(board,N,M)

    return bfs(board,N,M,start,goal)



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