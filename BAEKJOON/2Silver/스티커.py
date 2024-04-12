# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/9465

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        N = int(input())
        stikers = [list(map(int, input().split())) for _ in range(2)]
        dp = [[0]*N for _ in range(2)]

        dp[0][0] = stikers[0][0]
        dp[1][0] = stikers[1][0]

        for j in range(N-1):
            for i in range(2):
                # i는 해당 라인, _i는 다른 라인
                _i = not i
                # 대각선 스티커를 선택
                dp[_i][j+1] = max(dp[i][j] + stikers[_i][j+1], dp[_i][j+1])
                # 대각선을 안뜯고 그 다음에 있는 스티커를 선택
                if j+2 >= N: continue
                dp[_i][j+2] = max(dp[i][j] + stikers[_i][j+2], stikers[_i][j+2])

        print(max(dp[0][N-1], dp[1][N-1]))