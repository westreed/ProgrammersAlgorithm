# 그래프 이론, 그래프 탐색, 너비 우선 탐색
# https://www.acmicpc.net/problem/7576

# 입력
'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
0 0 -1 0 0 0
0 -1 0 -1 -1 -1
-1 0 0 0 0 0
0 0 0 0 0 1
'''

from collections import deque
input = __import__('sys').stdin.readline
M, N = map(int, input().split())
Store = [list(map(int, input().split())) for _ in range(N)]
Days = 0
Empty = 0
Queue = deque()
Waits = deque()

for m in range(M):
    for n in range(N):
        if Store[n][m] != -1:
            Empty += 1
            if Store[n][m] == 1:
                Queue.append((m, n))

while True:
    while Queue:
        m, n = Queue.pop()
        if Store[n][m] != 2:
            Store[n][m] = 2
            Empty -= 1
        
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                mx = m + dx
                nx = n + dy

                if 0 <= mx < M and 0 <= nx < N:
                    if Store[nx][mx] == 0:
                        Store[nx][mx] = 1
                        Waits.append((mx, nx))

    if Waits:
        Days += 1
        Queue = Waits
        Waits = deque()

    else:
        if Empty: print(-1)
        else: print(Days)
        break
