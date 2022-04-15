# 위클리 챌린지
# https://programmers.co.kr/learn/courses/30/lessons/87377

INF = float('inf')

def findPoint(line1, line2):
    A,B,E,C,D,F = *line1, *line2
    c = (A*D)-(B*C)
    if c == 0: return INF,INF
    
    x1,y1 = (B*F)-(E*D),(E*C)-(A*F)
    return x1/c, y1/c

def solution(line):
    from itertools import combinations
    point_set = []
    combine_result = list(combinations(line,2))
    minX, minY = INF, INF
    maxX, maxY = -INF, -INF
    for l in combine_result:
        x,y = findPoint(l[0], l[1])
        if x != INF and y != INF:
            x1,y1 = int(x),int(y)
            if x == x1 and y == y1:
                minX, minY = min(minX, x1), min(minY, y1)
                maxX, maxY = max(maxX, x1), max(maxY, y1)
                point_set.append((x1,y1))
    
    sizeX, sizeY = maxX-minX+1, maxY-minY+1
    dot = [["." for _ in range(sizeX)] for _ in range(sizeY)]
    for x,y in point_set: dot[maxY-y][x-minX] = "*"
    return ["".join(d) for d in dot]

line = [
    [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]],
    [[0, 1, -1], [1, 0, -1], [1, 0, 1]],
    [[1, -1, 0], [2, -1, 0]],
    [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
]

result = [
    ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"],
    ["*.*"],
    ["*"],
    ["*"]
]

for q in [0,1,2,3]:
    qid = solution(line[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')