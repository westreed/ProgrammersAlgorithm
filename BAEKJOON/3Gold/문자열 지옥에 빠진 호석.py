# 
# https://www.acmicpc.net/problem/20166

import sys
from collections import defaultdict, deque

input = sys.stdin.readline
cnt = 0 # 최대 탐색 길이
N,M,K = map(int, input().split())
board = [list(input()) for _ in range(N)]
god_words = []
for _ in range(K):
    word = input().rstrip()
    cnt = max(cnt, len(word))
    god_words.append(word)

word_dict = defaultdict(int)
arrow = ((-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,-1),(-1,-1),(1,1))

def find(n, m):
    queue = deque([(n,m,board[n][m])])

    while queue:
        x,y,s = queue.pop()

        if len(s) <= cnt:
            word_dict[s] += 1
            if len(s) == cnt:
                continue

        for dx,dy in arrow:
            nx,ny = (x+dx)%N, (y+dy)%M
            queue.append((nx,ny,s+board[nx][ny]))

for n in range(N):
    for m in range(M):
        find(n, m)

answer = []
for god_word in god_words:
    answer.append(str(word_dict[god_word]))

print("\n".join(answer))