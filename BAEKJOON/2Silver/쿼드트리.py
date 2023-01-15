# 분할 정복, 재귀
# https://www.acmicpc.net/problem/1992

# 입력
'''
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
'''

input = __import__('sys').stdin.readline
N = int(input())
Image = [list(map(int, list(input().strip()))) for _ in range(N)]
Answer = ''

def Divsion(x, y, size):
    global Answer
    checking = True
    val = Image[y][x]
    for _x in range(x, x+size):
        for _y in range(y, y+size):
            if Image[_y][_x] != val:
                checking = False
                break
        if checking is False:
            break
    
    if checking:
        Answer += str(val)
        return True
    else:
        Answer += '('
        half = size // 2
        Divsion(x, y, half)
        Divsion(x+half, y, half)
        Divsion(x, y+half, half)
        Divsion(x+half, y+half, half)
        Answer += ')'


Divsion(0, 0, N)
print(Answer)