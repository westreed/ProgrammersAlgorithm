# 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# https://www.acmicpc.net/problem/1388

# 입력
'''
4 4
----
----
----
----

6 9
-||--||--
--||--||-
|--||--||
||--||--|
-||--||--
--||--||-

7 8
--------
|------|
||----||
|||--|||
||----||
|------|
--------

10 10
||-||-|||-
||--||||||
-|-|||||||
-|-||-||-|
||--|-||||
||||||-||-
|-||||||||
||||||||||
||---|--||
-||-||||||

6 6
-||--|
||||||
|||-|-
-||||-
||||-|
||-||-

정답
4
31
13
41
19
'''

import sys
input = sys.stdin.readline

Answer = 0
N, M = list(map(int, input().split()))
Board = []
for _ in range(N):
    Board.append(list(input().strip()))

def connectPiece(x, y):
    global N,M,Board

    if Board[y][x] == '-':
        for z in range(1, M-x):
            if Board[y][x+z] == '-':
                Board[y][x+z] = 0
            else:
                break

    else:
        for z in range(1, N-y):
            if Board[y+z][x] == '|':
                Board[y+z][x] = 0
            else:
                break
    Board[y][x] = 0

for y in range(N):
    for x in range(M):
        if Board[y][x] != 0:
            connectPiece(x, y)
            Answer += 1

print(Answer)
