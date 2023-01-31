# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/15645

# 입력
'''
3
1 2 3
4 5 6
4 9 0
'''

input = __import__('sys').stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
L = __import__('copy').deepcopy(S)

def find(N, S, T):
    cal = lambda x: max(x) if T else min(x)
    for i in range(1, N):
        S[i][0] += cal(S[i-1][:2])
        S[i][1] += cal(S[i-1])
        S[i][2] += cal(S[i-1][1:])
    return cal(S[N-1])

print(find(N, L, True), find(N, S, False))