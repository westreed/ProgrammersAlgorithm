# 구현, 브루트포스 알고리즘
# https://www.acmicpc.net/problem/18111

'''
3 4 11
29 51 54 44
22 44 32 62
25 38 16 2

출력: 정답 - 250, 35 // 출력: 214, 44

4 4 36
15 43 61 21
19 33 31 55
48 63 1 30
31 28 3 8

출력: 정답 - 355, 32 // 출력: 353, 33
'''

import sys
input = sys.stdin.readline

N,M,B = map(int, input().split())
landmap = []
minv, maxv = float('inf'), 0
for _ in range(N):
    _temp = list(map(int, input().split()))
    landmap.extend(_temp)

    t_minv = min(_temp)
    if t_minv < minv: minv = t_minv
    t_maxv = max(_temp)
    if t_maxv > maxv: maxv = t_maxv

answer = [float('inf'),-1]
for h in range(minv, maxv+1):
    remove = 0
    create = 0

    for m in landmap:
        if m > h:   remove += m-h
        elif m < h: create += h-m
    
    timer = (remove*2)+create
    if B+remove >= create and answer[0] >= timer and answer[1] < h:
        answer = [timer, h]
    
print(*answer)