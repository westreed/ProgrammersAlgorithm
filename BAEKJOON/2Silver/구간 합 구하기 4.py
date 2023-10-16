# 누적 합
# https://www.acmicpc.net/problem/11659

input = __import__('sys').stdin.readline

N, M = map(int, input().split())
Array = list(map(int, input().split()))

for n in range(1, N):
    Array[n] = Array[n]+Array[n-1]

for _ in range(M):
    start, end = map(int, input().split())
    answer = Array[end-1]
    if start > 1: answer -= Array[start-2]
    print(answer)