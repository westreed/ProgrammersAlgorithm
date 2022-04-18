# 월간 코드 챌린지 시즌3
# https://programmers.co.kr/learn/courses/30/lessons/86052

def cycle(M,N,x,y):
    x1,y1 = x,y
    if x < 0: x1 = M-1
    if x >= M: x1 = 0
    if y < 0: y1 = N-1
    if y >= N: y1 = 0
    return x1,y1

def setDirection(grid,direct,x,y):
    if grid[y][x] == 'S': return direct
    elif grid[y][x] == 'L':
        if direct == 0: return 3
        else: return direct-1
    else:
        if direct == 3: return 0
        else: return direct+1

def tracing(grid, M, N, start, direct):
    length = 0
    #point -> (0,0)
    point = start
    #direction -> 'U','D','L','R'
    direction = direct
    #path -> 'LRLLR...'
    path = []
    arrow = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
    while length == 0 or point != start or direction != direct:
        x,y = cycle(M,N,arrow[direction][0]+point[0],arrow[direction][1]+point[1])
        direction = setDirection(grid,direction,x,y)
        point = (x,y)
        length += 1
        path += [str(x)+str(y)+str(direction)]
    return [length, "".join(sorted(path))]

# def compare(path, cond):
#     #cond -> '10D'
#     value = cond[:3]
#     index = path.find(value)
#     if index:
#         temp = path[index:]+path[:index]
#         if temp == cond: return True
#     return False

def solution(grid):
    #M - x축, N - y축
    M,N = len(grid[0]),len(grid)
    answer = {}
    for y in range(N):
        for x in range(M):
            for d in range(4):
                length, path = tracing(grid, M, N, (x,y), d)
                answer[path] = length

    return sorted(list(answer.values()))

grid = [
    ["SL","LR"],
    ["S"],
    ["R", "R"]
]

result = [
    [16],
    [1,1,1,1],
    [4,4]
]

for q in [0,1,2]:
    qid = solution(grid[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')