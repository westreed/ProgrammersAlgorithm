# 구현, 자료 구조, 스택
# https://www.acmicpc.net/problem/10773

from collections import deque
input = __import__('sys').stdin.readline

Stack = deque()
for _ in range(int(input())):
    Number = int(input())

    if Number == 0: Stack.pop()
    else: Stack.append(Number)
    
print(sum(Stack))