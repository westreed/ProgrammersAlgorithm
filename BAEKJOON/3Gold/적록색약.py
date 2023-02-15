# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# https://www.acmicpc.net/problem/10026

# Try 1
# 34312 KB	92 ms

input = __import__('sys').stdin.readline
N = int(input())
RGB1 = []
RGB2 = []

for _ in range(N):
    data = input().strip()
    RGB1.append(list(data))
    RGB2.append(list(data.replace("G","R")))

CNT1 = {"R":0, "G":0, "B":0}
CNT2 = {"R":0, "B":0}

def bfs(Color, Board, Start, CNT):
    from collections import deque

    sx,sy = Start
    if Board[sy][sx] == 0: return False

    Queue = deque([Start])
    Board[sy][sx] = 0
    CNT[Color] += 1

    while Queue:
        cx,cy = Queue.popleft()
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < N and 0 <= ny < N:
                if Board[ny][nx] == Color:
                    Board[ny][nx] = 0
                    Queue.append((nx,ny))

for y in range(N):
    for x in range(N):
        bfs(RGB1[y][x], RGB1, (x,y), CNT1)
        bfs(RGB2[y][x], RGB2, (x,y), CNT2)

print(CNT1["R"]+CNT1["G"]+CNT1["B"], CNT2["R"]+CNT2["B"])
