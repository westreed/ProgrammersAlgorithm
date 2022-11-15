# 
# https://www.acmicpc.net/problem/16502

# 입력
'''
2
6
A B 1.0
B C 0.3
B D 0.7
C A 0.6
C D 0.4
D D 1.0

답
4.50
15.00
7.50
73.00
'''

from collections import defaultdict
input = __import__("sys").stdin.readline
N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    receive = input().split()
    receive[2] = float(receive[2])
    graph[receive[0]].append((receive[1], receive[2]))

print(graph)
    