# 그래프 이론, 그래프 탐색, 너비 우선 탐색
# https://www.acmicpc.net/problem/7562

'''
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
'''

from collections import deque
input = __import__('sys').stdin.readline
TestCase = int(input())
Direction = [(1,2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1)]


for _ in range(TestCase):
    Size = int(input())
    Sx,Sy = map(int, input().split())
    Tx,Ty = map(int, input().split())

    ChessMap = [[-1 for _ in range(Size)] for _ in range(Size)]

    ChessMap[Sy][Sx] = 0
    Queue = deque()
    Queue.append((Sx, Sy))

    while Queue:
        Nx, Ny = Queue.popleft()
        if Nx == Tx and Ny == Ty: break

        for Dx, Dy in Direction:
            Cx, Cy = Nx+Dx, Ny+Dy
            if 0 <= Cx < Size and 0 <= Cy < Size:
                if ChessMap[Cy][Cx] == -1:
                    ChessMap[Cy][Cx] = ChessMap[Ny][Nx]+1
                    Queue.append((Cx, Cy))
    

    print(ChessMap[Ty][Tx])


