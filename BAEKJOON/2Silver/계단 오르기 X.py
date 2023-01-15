# 
# https://www.acmicpc.net/problem/2579

# 입력
'''
6
10
20
15
25
10
20
'''

input = __import__('sys').stdin.readline
N = int(input())
Stair = [int(input()) for _ in range(N)]
DP = [(0,0) for _ in range(N)]

print(Stair)

for i in range(-1, N):
    score, jump = DP[i]
    if i+1 < N and jump < 2:
        _score = score + Stair[i+1]
        _jump = jump + 1
        if DP[i+1][0] <= _score and (DP[i+1][1] == 0 or DP[i+1][1] >= _jump):
            print(1)
            DP[i+1] = (_score, _jump)
    if i+2 < N:
        _score = score + Stair[i+2]
        _jump = 0
        if DP[i+2][0] <= _score and DP[i+2][1] >= _jump:
            print(2)
            DP[i+2] = (_score, _jump)
    print(DP)

# print(DP)