# 
# https://www.acmicpc.net/problem/9655

# 입력
'''
5

답
SK
'''

'''
4n 일땐, 창영이가 이김.
4n+1 일땐, 상근이가 이김.
4n+2 일땐, 창영이가 이김.
4n+3 일땐, 상근이가 이김.
'''

input = __import__("sys").stdin.readline
if int(input()) % 4 in [0, 2]: print("CY")
else: print("SK")