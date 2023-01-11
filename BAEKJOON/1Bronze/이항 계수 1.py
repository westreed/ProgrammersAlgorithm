# 수학, 구현, 조합론
# https://www.acmicpc.net/problem/11050

input = __import__('sys').stdin.readline
N, K = map(int, input().split())

Up = 1
Down = 1
for i in range(K): Up *= N-i
for i in range(K): Down *= (i+1)

print((Up//Down))