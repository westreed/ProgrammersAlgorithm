#
# https://www.acmicpc.net/problem/15724

# 입력
'''
4 4
9 14 29 7
1 31 6 13
21 26 40 16
8 38 11 23
4
1 1 3 2
1 1 1 4
1 1 4 4
3 3 4 4
'''

input = __import__('sys').stdin.readline
N, M = map(int, input().split())
Land = [list(map(int, input().split())) for _ in range(N)]

# → 방향으로 누적합
for n in range(N):
    for m in range(1, M):
        Land[n][m] += Land[n][m-1]

# ↓ 방향으로 누적합
for m in range(M):
    for n in range(1, N):
        Land[n][m] += Land[n-1][m]

# Trigger
for idx in range(int(input())):
    x1,y1,x2,y2 = map(int, input().split())
    sums = Land[x2-1][y2-1]

    if x1 > 1: sums -= Land[x1-2][y2-1]
    if y1 > 1: sums -= Land[x2-1][y1-2]
    if x1 > 1 and y1 > 1: sums += Land[x1-2][y1-2]
    print(sums)