# 자료구조, 스택
# https://www.acmicpc.net/problem/1874

from collections import deque
input = __import__('sys').stdin.readline

number = int(input())
stacks = deque()
orders = deque([i+1 for i in range(number)])
result = deque()
answer = deque([int(input()) for _ in range(number)])

index = 0
command = []
while answer:
    ans_node = answer.popleft()
    
    while index < ans_node:
        stacks.append(orders.popleft())
        index += 1
        command.append('+')
    
    if stacks[-1] == ans_node: 
        result.append(stacks.pop())
        command.append('-')
    else:
        print('NO')
        break

if not stacks:
    for cmd in command:
        print(cmd)