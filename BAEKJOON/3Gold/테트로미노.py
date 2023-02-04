# 구현, 브루트포스 알고리즘
# https://www.acmicpc.net/problem/14500

input = __import__('sys').stdin.readline
N, M = map(int, input().split())
Maps = [list(map(int, input().split())) for _ in range(N)]
MAX  = 0

Tetromino = {
    0: [[(0,0),(1,0),(0,1),(1,1)]], # ㅁ
    1: [[(0,0),(1,0),(2,0),(3,0)]], # ㅡ
    2: [[(0,0),(1,0),(2,0),(1,1)]], # ㅗ
    3: [[(0,0),(0,1),(0,2),(1,2)]], # ㄴ
    4: [[(0,0),(0,1),(1,1),(1,2)]]  # └┐
}

def rotate(arr):
    newPattern = []
    for i in range(4):
        newPattern.append((arr[i][1], -arr[i][0]))
    return newPattern

for t in range(1,5):
    # 90도 회전
    for r in range(3):
        Tetromino[t].append(rotate(Tetromino[t][-1]))

    if t < 3: continue
    # 대칭
    origin = Tetromino[t][0]
    Tetromino[t].append([(origin[i][0], -origin[i][1]) for i in range(4)])
    for r in range(3):
        Tetromino[t].append(rotate(Tetromino[t][-1]))

def find(arr, n, m):
    global Maps
    length = len(arr)
    _temp = 0
    for l in range(length):
        _score = 0
        for i in range(4):
            x,y = arr[l][i]
            _n, _m = n+x, m+y
            if 0 <= _n < N and 0 <= _m < M:
                _score += Maps[_n][_m]
            else:
                _score = -1
                break
        if _temp < _score: _temp = _score
    return _temp

for t in range(5):
    for n in range(N):
        for m in range(M):
            res = find(Tetromino[t], n, m)
            if res and MAX < res:
                MAX = res

print(MAX)