# 구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# https://www.acmicpc.net/problem/16173

# 입력
'''
3
1 1 10
1 5 1
2 2 -1

3
2 2 1
2 2 2
1 2 -1

답
HaruHaru
Hing
'''

import sys
input = sys.stdin.readline

N = int(input())
Maps = []
for _ in range(N):
    Maps.append(list(map(int, input().split())))

Check = False
Queue = []
Queue.append((0,0))

while Queue:
    cx, cy = Queue.pop()
    if (cx, cy) == (N-1, N-1):
        print("HaruHaru")
        Check = True
        break

    cnt = Maps[cy][cx]
    if cnt >= N or cnt == 0: continue
    if cx < N and cy+cnt < N:
        Queue.append((cx, cy+cnt))
    if cy < N and cx+cnt < N:
        Queue.append((cx+cnt, cy))

if Check is False:
    print("Hing")