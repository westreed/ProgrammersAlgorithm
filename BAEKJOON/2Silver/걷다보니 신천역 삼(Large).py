# 수학, 다이나믹 프로그래밍, 정수론
# https://www.acmicpc.net/problem/14651
def sam(N):
    if N == 1: return 0
    n = 2
    for _ in range(N-2):
        n *= 3
        n %= 1000000009
    return n

print(sam(int(input())))