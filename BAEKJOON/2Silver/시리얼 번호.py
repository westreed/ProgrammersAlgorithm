# 
# https://www.acmicpc.net/problem/1431

"""
5
ABCD
145C
A
A910
Z321
"""

import sys

input = sys.stdin.readline
N = int(input())
lists = []
for _ in range(N):
    serial = input().rstrip()
    serial_len = len(serial)
    serial_sum = 0
    for i in serial:
        if i.isdigit():
            serial_sum += int(i)
    
    lists.append((serial_len, serial_sum, serial))

lists.sort()
print("\n".join(list(map(lambda x: x[2], lists))))