# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/2193

dp = [0, 1, 1]
for i in range(2, int(input())):
    dp.append(dp[i]+dp[i-1])
print(dp[-1])