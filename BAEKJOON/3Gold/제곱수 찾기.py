# 브루트포스 알고리즘
# https://www.acmicpc.net/problem/1025

input = __import__('sys').stdin.readline
N, M = map(int, input().split())
Table = [list(map(int, list(input().strip()))) for _ in range(N)]
res = -1

for cx in range(N):
    for cy in range(M):
        for dx in range(-N, N+1):
            for dy in range(-M, M+1):
                # 둘다 0이면, 값 1개만 읽음.
                if dx == 0 and dy == 0: continue
                px, py = cx, cy

                temp = ''
                while (0 <= px < N) and (0 <= py < M):
                    temp += str(Table[px][py])
                    px += dx
                    py += dy

                    val = int(temp)
                    square = int(val)**0.5
                    if int(square) == square and res < val:
                        res = val

print(res)