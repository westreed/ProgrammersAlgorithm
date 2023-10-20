# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/1149

input = __import__('sys').stdin.readline
INF = 1e9
N = int(input())
Paint = {house : tuple(map(int, input().split())) for house in range(N)}

DP = [[INF,INF,INF] for _ in range(N)]
DP[0] = Paint[0]

for n in range(0, N-1):
    for cur_color in range(3):
        for nxt_color in range(3):
            if cur_color != nxt_color:
                DP[n+1][nxt_color] = min(DP[n+1][nxt_color], DP[n][cur_color]+Paint[n+1][nxt_color])

print(DP)
print(min(DP[-1]))