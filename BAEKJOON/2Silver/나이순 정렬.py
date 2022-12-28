# 정렬
# https://www.acmicpc.net/problem/10814

input = __import__('sys').stdin.readline
[print(*member) for member in sorted([input().split() for _ in range(int(input()))], key=lambda x:int(x[0]))]