# 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색
# https://www.acmicpc.net/problem/12852

N = int(input())
dp = [None]*(int(1e6)+1)
dp[1] = (0, [1])
dp[2] = (1, [2,1])
dp[3] = (1, [3,1])

for n in range(4, N+1):
    c = [(dp[n-1][0]+1, [n] + dp[n-1][1])]
    d2 = n/2
    if int(d2) == d2:
        d2 = int(d2)
        c.append((dp[d2][0]+1, [n] + dp[d2][1]))
    d3 = n/3
    if int(d3) == d3:
        d3 = int(d3)
        c.append((dp[d3][0]+1, [n] + dp[d3][1]))
    c = min(c)
    dp[n] = c

print(dp[N][0])
print(*dp[N][1])