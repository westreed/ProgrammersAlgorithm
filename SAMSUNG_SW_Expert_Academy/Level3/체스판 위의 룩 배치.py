# 15612
# 연습문제

# 입력
'''
3
......O.
.......O
...O....
O.......
....O...
..O.....
.O......
.....O..
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
.O.O.O.O
O.O.O.O.
........
........
........
........
........
........
'''

ans = []
tc = int(input())
for t in range(tc):
    Maps = []
    for m in range(8):
        line = list(input().strip())
        Maps.append(line)
    
    Rook_Cnt = 0
    Rook_BRK = 0
    Rook_Row = 0
    Rook_Col = 0
    for i in range(8):
        Rook_BRK = 0
        for j in range(8):
            if Maps[i][j] == '.': continue
            Rook_Cnt += 1
            if Rook_Cnt > 8:
                Rook_BRK = 1
                break

            Row = pow(2, i)
            if Rook_Row & Row:
                Rook_BRK = 1
                break

            Col = pow(2, j)
            if Rook_Col & Col:
                Rook_BRK = 1
                break

            Rook_Row += Row
            Rook_Col += Col

        if Rook_BRK:
            ans.append(f"#{t+1} no")
            break
    
    if Rook_BRK == 0:
        if Rook_Cnt == 8:
            ans.append(f"#{t+1} yes")
        else:
            ans.append(f"#{t+1} no")

for t in range(tc):
    print(ans[t])