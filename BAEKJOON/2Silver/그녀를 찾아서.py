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
from copy import deepcopy
input = __import__("sys").stdin.readline

N = int(input())
M = int(input())
graph = defaultdict(list)
percent = {'A':25.0, 'B':25.0, 'C':25.0, 'D':25.0}
for _ in range(M):
    receive = input().split()
    receive[2] = float(receive[2])
    graph[receive[1]].append((receive[0], receive[2]))

for _ in range(N):
    _percent = deepcopy(percent)
    for d in ['A','B','C','D']:
        temp = sum(map(lambda x : _percent[x[0]]*x[1] , graph[d]))
        percent[d] = temp

for d in ['A','B','C','D']:
    print(f"{percent[d]:.2f}")