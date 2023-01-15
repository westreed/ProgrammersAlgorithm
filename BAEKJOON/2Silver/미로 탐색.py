# 그래프 이론, 그래프 탐색, 너비 우선 탐색
# https://www.acmicpc.net/problem/2178

# 입력
'''
4 6
101111
101010
101011
111011
'''

from collections import deque
input = __import__('sys').stdin.readline
N, M = map(int, input().split())
Maps = [list(map(int, list(input().strip()))) for _ in range(N)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

Queue = deque()
Queue.append((0,0))

while Queue:
    cx, cy = Queue.popleft()

    if cx == M-1 and cy == N-1:
        print(Maps[N-1][M-1])
        break

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if Maps[ny][nx] == 1:
                Maps[ny][nx] = Maps[cy][cx] + 1
                Queue.append((nx, ny))