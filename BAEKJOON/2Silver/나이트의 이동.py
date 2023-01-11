# 
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

input = __import__('sys').stdin.readline
TestCase = int(input())
Direction = [(1,2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1)]

for _ in range(TestCase):
    Size = int(input())
    Sx,Sy = map(int, input().split())
    Tx,Ty = map(int, input().split())

    ChessMap = [[-1 for _ in range(Size)] for _ in range(Size)]

    ChessMap[Sy][Sx] = 0
    Queue = []
    Queue.append((Sx, Sy))

    while Queue:
        Nx, Ny = Queue.pop(0)
        Cnt = ChessMap[Ny][Nx]
        CenterRng = abs(Nx-Tx)+abs(Ny-Ty)

        for Dx, Dy in Direction:
            Cx, Cy = Nx+Dx, Ny+Dy
            if 0 <= Cx < Size and 0 <= Cy < Size:
                if ChessMap[Cy][Cx] == -1 or ChessMap[Cy][Cx] > Cnt:
                    if abs(Cx-Tx)+abs(Cy-Ty) <= CenterRng:
                        ChessMap[Cy][Cx] = Cnt+1
                        Queue.append((Cx, Cy))
        
        # print(f"Queue:{len(Queue)} {Nx},{Ny}")
        # for m in ChessMap:
        #     for m1 in m:
        #         print(f"{m1:02} ", end='')
        #     else:
        #         print()


    print(ChessMap[Ty][Tx])


