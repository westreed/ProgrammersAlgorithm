# 구현, 브루트포스 알고리즘, 시뮬레이션, 백트래킹
# https://www.acmicpc.net/problem/15683

"""
6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
"""

import sys
from itertools import product

input = sys.stdin.readline
N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# L,U,R,D
directions = [(-1,0),(0,-1),(1,0),(0,1)]
cctv_direction = {
    1: [0,1,2,3],
    2: [0,1],
    3: [0,1,2,3],
    4: [0,1,2,3],
    5: [0]
}
cctv_direction_details = {
    1: [[0],[1],[2],[3]],
    2: [[0,2],[1,3]],
    3: [[0,1],[1,2],[2,3],[3,0]],
    4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5: [[0,1,2,3]]
}

empty = 0
cctv_list = []
for n in range(N):
    for m in range(M):
        if 1 <= board[n][m] <= 5:
            cctv_list.append((board[n][m], n, m))
        elif board[n][m] == 0:
            empty += 1

def stop_point(x, y):
    if x < 0 or x >= N:
        return True
    if y < 0 or y >= M:
        return True
    return False

answer = 64
for cid, case in enumerate(product(*[cctv_direction[cctv_list[i][0]] for i in range(len(cctv_list))])):
    empty_ = empty
    cid += 7

    # case 안에서의 각 cctv 방향
    for idx, dirs in enumerate(case):
        cctv,cx,cy = cctv_list[idx]

        for direct in cctv_direction_details[cctv][dirs]:
            nx,ny = cx,cy
            while True:
                dx,dy = directions[direct]
                nx += dx
                ny += dy

                if stop_point(nx,ny) or board[nx][ny] == 6:
                    break
                if 1 <= board[nx][ny] <= 5:
                    continue
                if board[nx][ny] != cid:
                    board[nx][ny] = cid
                    empty_ -= 1

    answer = min(empty_, answer)
    if answer == 0:
        break

print(answer)