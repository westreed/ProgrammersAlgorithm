# 정렬
# https://www.acmicpc.net/problem/10989

input = __import__('sys').stdin.readline
Lists = [0 for _ in range(10000+1)]

for _ in range(int(input())):
    Lists[int(input())] += 1

for i in range(10000+1):
    if not Lists[i]: continue
    for j in range(Lists[i]):
        print(i)