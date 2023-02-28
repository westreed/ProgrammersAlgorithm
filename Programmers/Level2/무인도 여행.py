# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

def solution(maps):
    SIZE_X = len(maps[0])
    SIZE_Y = len(maps)
    
    for y in range(SIZE_Y):
        maps[y] = list(map(lambda x: 0 if x == 'X' else int(x), maps[y]))
    
    def bfs(x,y):
        from collections import deque

        Arrow = ((1,0),(-1,0),(0,1),(0,-1))
    
        Foods = maps[y][x]
        maps[y][x] = 0
        Queue = deque([(x,y)])

        while Queue:
            cx,cy = Queue.popleft()
            for dx, dy in Arrow:
                nx, ny = cx+dx, cy+dy
                
                if 0 > nx or nx >= SIZE_X: continue
                if 0 > ny or ny >= SIZE_Y: continue
                if maps[ny][nx] > 0:
                    Foods += maps[ny][nx]
                    maps[ny][nx] = 0
                    Queue.append((nx,ny))
        return Foods
    
    answer = []
    for y in range(SIZE_Y):
        for x in range(SIZE_X):
            if maps[y][x] > 0:
                answer.append(bfs(x,y))
    
    if answer: answer.sort()
    else: answer.append(-1)
    return answer

maps = [
    ["X591X","X1X5X","X231X", "1XXX1"],
    ["XXX","XXX","XXX"]
]

result = [
    [1, 1, 27],
    [-1]
]

for q in [0, 1]:
    qid = solution(maps[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')