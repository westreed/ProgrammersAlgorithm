# 다이나믹 프로그래밍, 슬라이딩 윈도우
# https://www.acmicpc.net/problem/2096

def dp_max(N, dp, board):
    dp[0] = board[0][:]
    idx = 0
    for n in range(N-1):
        idx = (n+1) % 2
        prev = 1 if idx == 0 else 0
        dp[idx][0] = max(dp[prev][0]+board[n+1][0], dp[prev][1]+board[n+1][0])
        dp[idx][1] = max(dp[prev][0]+board[n+1][1], dp[prev][1]+board[n+1][1], dp[prev][2]+board[n+1][1])
        dp[idx][2] = max(dp[prev][1]+board[n+1][2], dp[prev][2]+board[n+1][2])

    print(max(dp[idx]), end=" ")

def dp_min(N, dp, board):
    dp[0] = board[0][:]
    idx = 0
    for n in range(N-1):
        idx = (n+1) % 2
        prev = 1 if idx == 0 else 0
        dp[idx][0] = min(dp[prev][0]+board[n+1][0], dp[prev][1]+board[n+1][0])
        dp[idx][1] = min(dp[prev][0]+board[n+1][1], dp[prev][1]+board[n+1][1], dp[prev][2]+board[n+1][1])
        dp[idx][2] = min(dp[prev][1]+board[n+1][2], dp[prev][2]+board[n+1][2])
    
    print(min(dp[idx]))


if __name__ == "__main__":
    input = __import__("sys").stdin.readline
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0,0,0], [0,0,0]]
    dp_max(N, dp, board)
    dp_min(N, dp, board)