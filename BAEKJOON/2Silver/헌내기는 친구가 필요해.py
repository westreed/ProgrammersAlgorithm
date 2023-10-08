# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# https://www.acmicpc.net/problem/21736

from collections import deque

input = __import__("sys").stdin.readline
N, M = map(int, input().split())

answer = 0
arrow = ((-1, 0), (1, 0), (0, -1), (0, 1))
queue = deque()
Maps = []
Visit = [[False for _ in range(M)] for _ in range(N)]

for n in range(N):
    _case = input().rstrip()
    Maps.append(_case)
    if "I" in _case:
        m = _case.index("I")
        Visit[n][m] = True
        queue.append((n, m))

while queue:
    x,y = queue.popleft()

    for dx, dy in arrow:
        nx, ny = x+dx, y+dy
        
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if Visit[nx][ny]: continue
        if Maps[nx][ny] == "X": continue
        if Maps[nx][ny] == "P": answer += 1
        Visit[nx][ny] = True
        queue.append((nx,ny))

print(answer if answer > 0 else "TT")