# BFS, DFS
# https://www.acmicpc.net/problem/1012

# 입력
'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''


def bfs(s:list, maps:list, cabb:list, M:int, N:int):
    from collections import deque

    queue = deque()
    queue.append(s)
    maps[s[1]][s[0]] = 2

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while queue:
        x,y = queue.popleft()

        for d in range(4):
            px = x + dx[d]
            py = y + dy[d]

            if px < 0 or px >= M or py < 0 or py >= N: continue
            if maps[py][px] == 1:
                maps[py][px] = 2
                cabb.remove([px,py])
                queue.append([px,py])
                
answer = ''
for _ in range(int(input())):
    M,N,K = map(int, input().split())
    maps = [[0 for _ in range(M)] for _ in range(N)]
    cabb = []
    ans  = 0
    for k in range(K):
        x,y = map(int, input().split())
        maps[y][x] = 1
        cabb.append([x,y])
    
    while cabb:
        x,y = cabb.pop()
        bfs([x,y], maps, cabb, M, N)
        ans += 1
    
    answer += f'{ans}\n'

print(answer)