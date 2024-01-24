# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/11053

"""
6
10 50 20 30 40 50
answer 5

9
10 100 100 100 100 20 30 40 50
answer 5

20
322 831 212 232 545 698 260 265 324 215 701 75 156 605 851 993 425 887 691 593
answer 8
"""

if __name__ == "__main__":
    N = int(input())
    num_seq = list(map(int, input().split()))
    num_dp = [1] * N

    for i in range(N-1):
        for j in range(i+1, N):
            if num_seq[i] < num_seq[j]:
                num_dp[j] = max(num_dp[i]+1, num_dp[j])
    
    print(max(num_dp))