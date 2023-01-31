# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# https://www.acmicpc.net/problem/2667

# 입력
'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

input = __import__('sys').stdin.readline
N = int(input())
Maps = [list(map(int, list(input().strip()))) for _ in range(N)]

def find(Maps:list, x:int, y:int) -> int:
    from collections import deque

    global N
    idx = Maps[y][x]
    Maps[y][x] = 0
    cnt = 1

    Queue = deque()
    Queue.append((x, y))

    while Queue:
        cx, cy = Queue.popleft()

        for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < N and 0 <= ny < N:
                if Maps[ny][nx] == idx:
                    cnt += 1
                    Maps[ny][nx] = 0
                    Queue.append((nx, ny))
    
    return cnt

AreaCount = 0
AreaZone  = []
for y in range(N):
    for x in range(N):
        if Maps[y][x]:
            cnt = find(Maps, x, y)
            AreaZone.append(cnt)
            AreaCount += 1

print(AreaCount)
if AreaZone:
    AreaZone.sort()
    for zone in AreaZone:
        print(zone)