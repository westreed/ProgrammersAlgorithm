# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/1577

input = __import__('sys').stdin.readline
N, M = map(int, input().split())
N2, M2 = N*2, M*2
K = int(input())
Maps = [[0 for _ in range(N2+1)] for _ in range(M2+1)]
Maps[0][0] = 1

# 공사 위치 표시하기
for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    if x1 != x2:
        if x1 > x2: x1, x2 = x2, x1
        Maps[y1*2][x2*2 - 1] = -1
    elif y1 != y2:
        if y1 > y2: y1, y2 = y2, y1
        Maps[y2*2 - 1][x1*2] = -1

# 경우의 수가 1인 경로
for i in range(2, N2+1, 2):
    if Maps[0][i-2] > 0 and Maps[0][i-1] == 0: Maps[0][i] = 1
    else: break # 한번 끊어지면, 그 뒤로는 0임

for i in range(2, M2+1, 2):
    if Maps[i-2][0] > 0 and Maps[i-1][0] == 0: Maps[i][0] = 1
    else: break

# 최단거리 경우의 수 구하기
for y in range(2, M2+1, 2):
    for x in range(2, N2+1, 2):
        right, up = Maps[y][x-1], Maps[y-1][x]
        if right == up == -1: continue
        elif right == -1: Maps[y][x] = Maps[y-2][x]
        elif up == -1: Maps[y][x] = Maps[y][x-2]
        else: Maps[y][x] = Maps[y-2][x] + Maps[y][x-2]

print(Maps[M2][N2])
# for m in Maps[::2]:
#     print(m[::2])

for m in Maps:
    for s in m:
        print(s, end='\t')
    print()