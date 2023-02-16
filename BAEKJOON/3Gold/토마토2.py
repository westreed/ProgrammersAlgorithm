# 그래프 이론, 그래프 탐색, 너비 우선 탐색
# https://www.acmicpc.net/problem/7569

# Try 1
# 52552 KB	3516 ms

input = __import__('sys').stdin.readline
M,N,H = map(int, input().split())

from collections import deque

Queue = deque()
Waits = deque()
Board = []
Arrow = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
Unripe = 0
Answer = 0

for h in range(H):
    Floor = []
    for n in range(N):
        data = list(map(int, input().split()))
        for m in range(M):
            if data[m] == 1: Waits.append([m,n,h])
            elif data[m] == 0: Unripe += 1
        Floor.append(data)
    Board.append(Floor)

while True:
    if Waits and Unripe:
        Queue = Waits
        Waits = deque()
        Answer += 1
    
    else:
        if Unripe: print(-1)
        else: print(Answer)
        break

    while Queue:
        x,y,z = Queue.pop()

        for dx,dy,dz in Arrow:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if Board[nz][ny][nx] == 0:
                    Board[nz][ny][nx] = 1
                    Unripe -= 1
                    Waits.append([nx,ny,nz])