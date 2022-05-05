# 수학, 구현
# https://www.acmicpc.net/problem/10818

length = int(input())
lists = list(map(int, input().split()))

maxv, minv = -1000000, 1000000
for i in lists:
    if i > maxv: maxv = i
    if i < minv: minv = i
print(f'{minv} {maxv}')