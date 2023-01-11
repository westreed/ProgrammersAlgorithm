# 11315
# 연습문제

# 입력
'''
4
5
....o
...o.
..o..
.o...
o....
5
...o.
ooooo
...o.
...o.
.....
5
.o.oo
oo.oo
.oo..
.o...
.o...
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.
'''

def bfs(s, maps, N):
    from copy import deepcopy
    from collections import deque

    queue = deque()
    _maps = deepcopy(maps)
    _maps[s[1]][s[0]] = 1
    number = 1

    dx = [0,0,1,-1,1,-1,1,-1]
    dy = [1,-1,0,0,1,1,-1,-1]
    
    for d in range(8):
        queue.append(s + [d])

    while queue:
        x,y,d = queue.popleft()

        px = x + dx[d]
        py = y + dy[d]

        if px < 0 or px >= N or py < 0 or py >= N: continue
        if _maps[py][px] == 'o':
            value = _maps[y][x]+1
            if number < value: number = value
            _maps[py][px] = _maps[y][x]+1
            queue.append([px,py,d])
    
    print(f'출발위치 {s}')
    for i in _maps:
        for j in i:
            print(j, end='\t')
        print()

    return number

case = int(input())
for c in range(case):
    N = int(input())
    maps = []
    for i in range(N):
        maps.append(list(input().strip()))
    
    for i in range(N*N):
        x = i % N
        y = i // N
        if maps[y][x] == 'o':
            v = bfs([x,y], maps, N)
            if v >= 5:
                print(f'#{c+1} YES')
                break
    else:
        print(f'#{c+1} NO')