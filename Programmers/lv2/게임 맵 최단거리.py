# 찾아라 프로그래밍 마에스터
# https://programmers.co.kr/learn/courses/30/lessons/1844

def bfs(maps, M, N, y, x):

    queue = [[y, x, 2, f'{x},{y} → ']]
    maps[y][x] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:

        y, x, cnt, path = queue.pop(0)
        if y == N-1 and x == M-1: continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>=0 and nx < M and ny>=0 and ny < N:
                if maps[ny][nx] == 1:
                    maps[ny][nx] = cnt
                    queue.append([ny, nx, cnt+1, f'{path}{nx},{ny} → '])
    
    return 0, '경로없음'
    

def solution(maps):
    gx = len(maps[0])-1
    gy = len(maps)-1
    cnt, path = bfs(maps, gx+1, gy+1, 0, 0)
    print(cnt, path)
    if maps[gy][gx] <= 1:
        return -1
    else:
        return maps[gy][gx]

maps = [
    [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]],
    [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
]
result = [
    11,
    -1
]

for q in [0,1]:
    qid = solution(maps[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')