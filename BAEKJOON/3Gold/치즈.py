# 구현, 그래프 이론, 그래프 탐색, 시뮬레이션, 너비 우선 탐색, 깊이 우선 탐색
# https://www.acmicpc.net/problem/2638

def cheeze(N,M,board,visit,visit_flag):
    from collections import deque

    queue = deque([(0,0)])
    surface = deque()
    arrow = ((-1,0),(1,0),(0,-1),(0,1))
    is_air = 0

    while queue:
        x,y = queue.popleft()

        for dx,dy in arrow:
            nx,ny = dx+x, dy+y

            if nx < 0 or nx >= N: continue
            if ny < 0 or ny >= M: continue
            if visit[nx][ny] == visit_flag: continue

            if board[nx][ny]:
                if board[nx][ny] == 1:
                    surface.append((nx,ny))
                board[nx][ny] += 1
            else:
                is_air += 1
                visit[nx][ny] = visit_flag
                queue.append((nx,ny))
    
    while surface:
        x,y = surface.popleft()
        if board[x][y] == 2:
            board[x][y] = 1
        elif board[x][y] >= 3:
            board[x][y] = 0
    
    if N*M == is_air:
        return True
    else:
        return False


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N,M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit_flag = 1
    flow_hour = 0

    while True:
        if cheeze(N,M,board,visit,visit_flag):
            print(flow_hour)
            break
        else:
            visit_flag += 1
            flow_hour += 1



