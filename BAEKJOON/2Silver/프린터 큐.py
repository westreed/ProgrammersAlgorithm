# 구현, 자료구조, 시뮬레이션, 큐
# https://www.acmicpc.net/problem/1966

import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    lists = deque(map(int, input().split()))
    order = deque([i+1 for i in range(N)])

    seq = 0
    while lists:
        back = False
        li, od = lists.popleft(), order.popleft()
        for l,o in zip(lists, order):
            if li < l:
                lists.append(li)
                order.append(od)
                back = True
                break
        if back is True: continue

        seq += 1
        if od-1 == M:
            print(seq)
            break