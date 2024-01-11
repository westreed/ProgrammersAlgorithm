# 그래프 이론, 그래프 탐색, 너비 우선 탐색
# https://www.acmicpc.net/problem/2206

def bfs(N, M, board):
    from collections import deque

    INF = 0xFFFFFFFF
    # x,y,is_crash
    queue = deque([(0,0,False)])
    visit = [[[INF,INF] for _ in range(M)] for _ in range(N)]
    visit[0][0] = [1,1]
    direction = ((-1,0),(1,0),(0,-1),(0,1))

    while queue:
        x, y, is_crash = queue.popleft()

        if x == N-1 and y == M-1:
            return min(visit[x][y])
        
        for dx, dy in direction:
            nx, ny = dx+x, dy+y

            if 0 > nx or nx >= N: continue
            if 0 > ny or ny >= M: continue

            if visit[nx][ny][is_crash] != INF: continue

            if board[nx][ny]:
                if is_crash is False:
                    visit[nx][ny][1] = visit[x][y][is_crash]+1
                    queue.append((nx,ny,True))
            else:
                visit[nx][ny][is_crash] = visit[x][y][is_crash]+1
                queue.append((nx,ny,is_crash))

    return -1


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = [list(map(int, list(input().rstrip()))) for _ in range(N)]

    res = bfs(N,M,board)
    print(res)
