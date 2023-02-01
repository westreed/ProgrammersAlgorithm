# 다이나믹 프로그래밍, 자료 구조, 해시를 사용한 집합과 맵
# https://www.acmicpc.net/problem/1351

# A0 = 1
# Ai = A⌊i/P⌋ + A⌊i/Q⌋ (i ≥ 1)
# ⌊x⌋는 x를 넘지 않는 가장 큰 정수이다.

from collections import defaultdict
N,P,Q = map(int, input().split())
A = defaultdict(int)
A[0] = 1

def find(n):
    if A[n]: return A[n]
    A[n] = find(n//P) + find(n//Q)
    return A[n]

print(find(N))
print(A)