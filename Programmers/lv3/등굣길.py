# 동적계획법(Dynamic Programming)
# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    maps = [[0 for _ in range(m)] for _ in range(n)]

    for y in range(n):
        if [1, y+1] in puddles:
            break
        maps[y][0] = 1
    
    for x in range(m):
        if [x+1, 1] in puddles:
            break
        maps[0][x] = 1

    for y in range(1,n):
        for x in range(1, m):
            if [x+1,y+1] in puddles:
                maps[y][x] = 0
                continue
            maps[y][x] = maps[y][x-1]+maps[y-1][x]
    
    for map in maps:
        print(map)
    
    return maps[n-1][m-1] % 1000000007


m = [
    4,
    6,
    5,

]
n = [
    3,
    3,
    4
]
puddles=[
    [[2, 2]],
    [[2, 2], [4, 2]],
    [[2,1],[2,2],[2,3],[4,2],[4,3],[4,4]]
]
result = [
    4,
    5,
    1
]

for q in [0,1,2]:
    qid = solution(m[q], n[q], puddles[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')