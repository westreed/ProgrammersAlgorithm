# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/159993

def bfs(start, goal, maps, sizeX, sizeY, stand):
    ARROW = ((1,0),(-1,0),(0,1),(0,-1))
    from collections import deque
    
    Queue = deque([start])
    maps[start[1]][start[0]] = stand+1
    while Queue:
        cx,cy = Queue.popleft()
        if (cx,cy) == goal: return maps[cy][cx]-stand-1
        
        for dx, dy in ARROW:
            nx, ny = cx+dx, cy+dy
            if nx < 0 or nx >= sizeX: continue
            if ny < 0 or ny >= sizeY: continue
            if 0 <= maps[ny][nx] <= stand:
                maps[ny][nx] = maps[cy][cx]+1
                Queue.append((nx,ny))
        

def solution(maps):
    SIZE_X = len(maps[0])
    SIZE_Y = len(maps)
    START, END, LEVER = 0, 0, 0
    T = {"S":0, "E":0, "L":0, "O":0, "X":-1}
    
    for y in range(SIZE_Y):
        maps[y] = list(maps[y])
        for x in range(SIZE_X):
            C = maps[y][x]
            if START == 0 and C == "S": START = (x,y)
            if END == 0 and C == "E": END = (x,y)
            if LEVER == 0 and C == "L": LEVER = (x,y)
            maps[y][x] = T[C]
    
    CNT1 = bfs(START, LEVER, maps, SIZE_X, SIZE_Y, 0)
    if CNT1 is None: return -1
    CNT2 = bfs(LEVER, END, maps, SIZE_X, SIZE_Y, 10000)
    if CNT2 is None: return -1
    return CNT1+CNT2

maps = [
    ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"],
    ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
]

result = [
    16, -1
]

for q in [0,1]:
    qid = solution(maps[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')