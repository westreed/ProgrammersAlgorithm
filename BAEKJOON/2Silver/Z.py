# 분할 정복, 재귀
# https://www.acmicpc.net/problem/1074

# 입력
'''
2 3 1
3 7 7
1 0 0
4 7 7
10 511 511
10 512 512
'''

N,r,c = map(int, input().split())
answer = 0

def find(x, y, size):
    global answer
    if answer == -1: return
    if c == x and r == y:
        print(answer)
        answer = -1
        return
    
    if c < x + size and r < y + size:
        half = size//2
        find(x, y, half)
        find(x+half, y, half)
        find(x, y+half, half)
        find(x+half, y+half, half)
    else:
        answer += pow(size, 2)

find(0,0,pow(2,N))