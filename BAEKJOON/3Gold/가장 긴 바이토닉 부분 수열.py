# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/11054

"""
10
1 5 2 1 4 3 4 5 2 1
> 7
"""

if __name__ == "__main__":
    N = int(input())
    num_seq = list(map(int, input().split()))

    INS = 0
    DEC = 1
    dp = [[1]*N for _ in range(2)] # 0INS 1DEC

    for i in range(N):
        for j in range(i+1, N):
            if num_seq[i] < num_seq[j]:
                dp[INS][j] = max(dp[INS][i]+1, dp[INS][j])

            elif num_seq[i] > num_seq[j]:
                # 1. 증가하다가 감소한 경우
                # 2. 감소가 이어지는 경우
                dp[DEC][j] = max(dp[INS][i]+1, dp[DEC][i]+1, dp[DEC][j])

    print(max(dp[DEC]))