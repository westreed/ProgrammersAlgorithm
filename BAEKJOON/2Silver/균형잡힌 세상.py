# 자료 구조, 문자열, 스택
# https://www.acmicpc.net/problem/4949

# 입력
'''
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
'''

from collections import deque
input = __import__('sys').stdin.readline

while True:
    StringText = input()[:-1]
    if StringText == '.': break

    Stack = deque()
    for string in StringText:
        if string in ['(', ')', '[', ']']:
            Stack.append(string)
        
        if len(Stack) >= 2:
            if Stack[-2] == '(' and Stack[-1] == ')':
                Stack.pop()
                Stack.pop()
            elif Stack[-2] == '[' and Stack[-1] == ']':
                Stack.pop()
                Stack.pop()
    
    if Stack:
        print('no')
    else:
        print('yes')