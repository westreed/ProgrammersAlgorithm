# 그리디 알고리즘, 정렬
# https://www.acmicpc.net/problem/11399

N = int(input())
P = list(map(int, input().split()))
P.sort()

T = P[0]
A = P[0]
for i in range(1, N):
    T += P[i]
    A += T

print(A)