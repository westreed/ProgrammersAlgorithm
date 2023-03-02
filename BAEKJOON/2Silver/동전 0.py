# 그리디 알고리즘
# https://www.acmicpc.net/problem/11047

input = __import__("sys").stdin.readline
N, K = map(int, input().split())
Coin = [int(input()) for _ in range(N)]

Answer, Index = 0, list(range(N))
while K:
    idx = Index[-1]
    if Coin[idx] > K:
        Index.pop()
        continue
    cnt = K // Coin[idx]
    K -= Coin[idx]*cnt
    Answer += cnt

print(Answer)