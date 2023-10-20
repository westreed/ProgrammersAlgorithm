# 다이나믹 프로그래밍, 브루트포스 알고리즘
# https://www.acmicpc.net/problem/17626


N = int(input())
R = 223+1
Square = [i**2 for i in range(R)]

def FourSquares(n):
    for i in Square:
        for j in Square:
            for k in Square:
                for l in Square:
                    if i+j+k+l == n:
                        cnt = 0
                        if i: cnt += 1
                        if j: cnt += 1
                        if k: cnt += 1
                        if l: cnt += 1
                        return cnt

print(FourSquares(N))