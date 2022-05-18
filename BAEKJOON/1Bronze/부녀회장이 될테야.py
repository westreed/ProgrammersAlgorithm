# 수학, 구현
# https://www.acmicpc.net/problem/2775

import sys
input = sys.stdin.readline

Apart = [[i for i in range(15)] for _ in range(15)]
for j in range(1,15):
    for k in range(2,15):
        Apart[j][k] = Apart[j-1][k]+Apart[j][k-1]

tc = int(input())
for _ in range(tc):
    K,N = int(input()),int(input())
    print(Apart[K][N])