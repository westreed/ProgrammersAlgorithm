# 그래프 이론, 그래프 탐색, 너비 우선 탐색
# https://www.acmicpc.net/problem/14940

from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split())
board = []
queue = deque()
arrow = ((-1, 0), (1, 0), (0, -1), (0, 1))

for n in range(N):
    lines = list(map(int, input().replace("1", "-1").split()))
    if 2 in lines:
        m = lines.index(2)
        lines[m] = 0
        queue.append((m, n, 0))
    board.append(lines)

while queue:
    x, y, cnt = queue.popleft()
    cnt += 1

    for dx, dy in arrow:
        nx, ny = x+dx, y+dy

        if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
        if board[ny][nx] == -1:
            board[ny][nx] = cnt
            queue.append((nx, ny, cnt))

for row in board:
    print(*row)