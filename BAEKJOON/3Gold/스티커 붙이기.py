# 구현, 브루트포스 알고리즘, 시뮬레이션
# https://www.acmicpc.net/problem/18808

import sys

input = sys.stdin.readline
N,M,K = map(int, input().split())
stickers = []
notebook = [[0]*M for _ in range(N)]
answer = 0

class Sticker:
    def __init__(self):
        R,C = map(int, input().split())
        self.R = R
        self.C = C
        self.S = []
        for _ in range(R):
            self.S.append(list(map(int, input().split())))
    
    def paste(self):
        global N, M
        for _ in range(4):
            NN,MM = N-self.R+1, M-self.C+1
            for n in range(NN):
                for m in range(MM):
                    if self.add_sticker(n, m):
                        return True
            self.rotate()
        
        return False

    def add_sticker(self, cr: int, cc: int):
        global N, M, notebook
        for r in range(self.R):
            for c in range(self.C):
                nr, nc = cr+r, cc+c

                if self.S[r][c] == 0:
                    continue
                if 0 > nr or nr >= N:
                    return False
                if 0 > nc or nc >= M:
                    return False
                if notebook[nr][nc] == 1:
                    return False
        self.change(cr, cc)
        return True
    
    def rotate(self):
        self.R, self.C = self.C, self.R
        self.S = list(zip(*self.S[::-1]))

    def change(self, cr: int, cc: int):
        global N, M, notebook, answer
        for r in range(self.R):
            for c in range(self.C):
                nr, nc = cr+r, cc+c
                if self.S[r][c] == 1:
                    notebook[nr][nc] = 1
                    answer += 1

for _ in range(K):
    sticker = Sticker()
    sticker.paste()

print(answer)