# 분할 정복, 재귀
# https://www.acmicpc.net/problem/2630

# 입력
'''
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
'''

input = __import__('sys').stdin.readline
N = int(input())
Paper = [list(map(int, list(input().split()))) for _ in range(N)]
White = 0
Blue  = 0

def Divsion(x, y, size):
    global White, Blue
    checking = True
    val = Paper[y][x]
    for _x in range(x, x+size):
        for _y in range(y, y+size):
            if Paper[_y][_x] != val:
                checking = False
                break
        if checking is False:
            break
    
    if checking:
        if val: Blue += 1
        else: White += 1
        return True
    else:
        half = size // 2
        Divsion(x, y, half)
        Divsion(x+half, y, half)
        Divsion(x, y+half, half)
        Divsion(x+half, y+half, half)


Divsion(0, 0, N)
print(White)
print(Blue)