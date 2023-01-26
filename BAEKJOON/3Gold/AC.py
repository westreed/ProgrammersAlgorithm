# 구현, 자료 구조, 문자열, 파싱, 덱
# https://www.acmicpc.net/problem/5430

# 입력
'''
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
'''

from collections import deque
input = __import__('sys').stdin.readline
T = int(input())

for _ in range(T):
    Trigger = list(input().rstrip())
    input()
    Array = input().rstrip()[1:-1]
    Array = deque(map(int, Array.split(','))) if Array else deque()
    State = False
    
    for Trg in Trigger:
        try:
            if Trg == 'R': State = not State # Toggle
            else:
                if State is False: Array.popleft()
                else: Array.pop()

        except:
            print('error')
            break
    else: 
        # error가 안떴을 때
        if State: Array.reverse()
        print(str(Array)[6:-1].replace(' ', ''))