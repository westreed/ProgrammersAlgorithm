# 
# https://www.acmicpc.net/problem/12865

"""
4 7
6 13
4 8
3 6
5 12
"""

if __name__ == "__main__":
    input = __import__("sys").stdin.readline
    N, K = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [[0] * N for _ in range(K+1)]

    for idx in range(N):
        for kg in range(1, K+1):
            item_kg, item_value = items[idx]
            if kg >= item_kg:
                # 가방에 해당 아이템을 넣을 수 있는 공간이 있을때
                if idx > 0:
                    dp[kg][idx] = max(dp[kg-item_kg][idx-1] + item_value, dp[kg][idx-1])
                else:
                    dp[kg][idx] = item_value
            elif idx > 0:
               dp[kg][idx] = dp[kg][idx-1]

    print(dp[K][N-1])