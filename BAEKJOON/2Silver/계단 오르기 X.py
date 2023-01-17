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
Score = 0

from collections import deque

Queue = deque()
Queue.append((0, 0, 0))

while Queue:
    idx, score, jump = Queue.popleft()

    if idx == N-1:
        if Score < score: Score = score
        continue

    if idx+1 < N and jump < 2:
        Queue.append((idx+1, score+Stair[idx+1], jump+1))
    
    if idx+2 < N:
        Queue.append((idx+2, score+Stair[idx+2], 0))

print(Score)