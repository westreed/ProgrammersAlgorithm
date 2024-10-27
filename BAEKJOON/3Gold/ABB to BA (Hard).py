# 자료 구조, 문자열, 스택
# https://www.acmicpc.net/problem/32293

"""
4
3
ABB
9
ABABABBBB
12
AAAAAABBBBBB
12
AAAABBBBBBBB

BA
BAABA
AAAABABA
ABAAA
"""

import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
A = []

def logic(size, stack1, stack2):
    if size > 1:
        if stack1[size] == "B" and stack1[size-1] == "B" and stack1[size-2] == "A":
            stack2.append("A")
            stack2.append("B")
            stack1.pop()
            stack1.pop()
            stack1.pop()
            return size-3
    return size

for _ in range(T):
    l = int(input())
    S = list(input().rstrip())

    size = -1
    stack1 = deque()
    stack2 = deque() # 삽입대기

    for s in S:
        size += 1
        stack1.append(s)

        if size < 2:
            continue
        
        size = logic(size, stack1, stack2)
        while stack2:
            size += 1
            stack1.append(stack2.pop())
            size = logic(size, stack1, stack2)
    
    A.append("".join(stack1))

print("\n".join(A))