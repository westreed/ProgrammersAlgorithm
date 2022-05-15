# 자료구조, 스택
# https://www.acmicpc.net/problem/1874
import sys
from collections import deque

input = sys.stdin.readline

number = int(input())
stacks = deque()
orders = deque([i+1 for i in range(number)])
lists  = []
for _ in range(number):
    lists.append(int(input()))

minv,maxv = lists[0],lists[0]

while orders:
    node = orders.popleft()

    if minv < node:
        pass
