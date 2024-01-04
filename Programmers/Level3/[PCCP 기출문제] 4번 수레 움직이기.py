# PCCP 기출문제
# https://school.programmers.co.kr/learn/courses/30/lessons/250134

def find_point(M,N,maze):
    red_start_point = None
    red_end_point = None
    blue_start_point = None
    blue_end_point = None

    for m in range(M):
        for n in range(N):
            if maze[m][n] == 1:
                red_start_point = (m,n)
            elif maze[m][n] == 2:
                blue_start_point = (m,n)
            elif maze[m][n] == 3:
                red_end_point = (m,n)
            elif maze[m][n] == 4:
                blue_end_point = (m,n)
    
    return red_start_point, red_end_point, blue_start_point, blue_end_point

def move_point(cur, end, visit, M, N, maze):
    if cur == end:
        return [cur]
    
    paths = []
    x,y = cur
    for nx, ny in ((-1,0), (1,0), (0,-1), (0,1)):
        dx, dy = x+nx, y+ny
        if dx < 0 or dx >= M: continue
        if dy < 0 or dy >= N: continue
        if maze[dx][dy] & visit: continue
        if maze[dx][dy] == 5: continue
        paths.append((dx,dy))
    
    return paths

def bfs(M, N, maze):
    from collections import deque
    from copy import deepcopy as copy

    red_start, red_end, blue_start, blue_end = find_point(M,N,maze)
    # queue | (red:(m ,n), blue:(m, n), turn, maze)
    queue = deque([(red_start, blue_start, 0, maze)])

    while queue:
        cur_red, cur_blue, t, _maze = queue.popleft()
        if cur_red == red_end and cur_blue == blue_end: return t
        
        r_m, r_n = cur_red
        b_m, b_n = cur_blue

        if _maze[r_m][r_n] < 5: _maze[r_m][r_n] = 0
        _maze[r_m][r_n] |= 0x8 # 8
        if _maze[b_m][b_n] < 5: _maze[b_m][b_n] = 0
        _maze[b_m][b_n] |= 0x10 # 16

        for next_red_m, next_red_n in move_point(cur_red, red_end, 0x8, M, N, _maze):
            for next_blue_m, next_blue_n in move_point(cur_blue, blue_end, 0x10, M, N, _maze):
                next_red = (next_red_m, next_red_n)
                next_blue = (next_blue_m, next_blue_n)

                if next_red == next_blue: continue
                if next_red == cur_blue and next_blue == cur_red: continue

                queue.append((next_red, next_blue, t+1, copy(_maze)))
    return 0


def solution(maze):
    M,N = len(maze), len(maze[0]) # 세로, 가로 크기

    # 0 빈칸
    # 1 빨간 친구 시작점
    # 2 파란 친구 시작점
    # 3 빨간 친구 도착점
    # 4 파란 친구 도착점
    # 5 벽
    # 6 방문한 칸 red:8 blue:16 (24이면 red,blue 모두 방문)
    return bfs(M,N,maze)




maze = [
    [[1, 4], [0, 0], [2, 3]],
    [[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]],
    [[1, 5], [2, 5], [4, 5], [3, 5]],
    [[4, 1, 2, 3]],
]

result = [
    3, 7, 0, 0
]

for q in [0,1,2,3]:
    qid = solution(maze[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')