# 자료 구조, 스택
# https://www.acmicpc.net/problem/1918

from collections import deque

infix_notation = input().strip()
stack = deque()
postfix_notation = ""

def PrecOperator(s):
    if s in ("*", "/"):
        return 2
    
    if s in ("+", "-"):
        return 1
    
    return 0

for s in infix_notation:
    if s.isalpha():
        postfix_notation += s

    elif s == "(":
        stack.append("(")

    elif s == ")":
        while stack and stack[-1] != "(":
            postfix_notation += stack.pop()
        stack.pop() # ( 제거

    # 연산자만 남음
    else:
        while stack and PrecOperator(stack[-1]) >= PrecOperator(s):
            postfix_notation += stack.pop()
        stack.append(s)

while stack:
    postfix_notation += stack.pop()

print(postfix_notation)