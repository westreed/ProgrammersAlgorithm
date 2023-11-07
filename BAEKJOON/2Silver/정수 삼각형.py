# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/1932

import sys

input = sys.stdin.readline

N = int(input())
inputs = [list(map(int, input().split())) for _ in range(N)]

DP = [[0 for _ in range(n+1)] for n in range(N)]
DP[0][0] = inputs[0][0]
for n in range(N-1):
    for i in range(n+1):
        DP[n+1][i] = max(DP[n][i] + inputs[n+1][i], DP[n+1][i])
        DP[n+1][i+1] = max(DP[n][i] + inputs[n+1][i+1], DP[n+1][i+1])

print(max(DP[-1]))