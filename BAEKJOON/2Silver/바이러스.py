# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# https://www.acmicpc.net/problem/2606

# 입력
'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7

답
4
'''

import sys
input = sys.stdin.readline

N = int(input()) # 컴퓨터수
M = int(input()) # 그래프
graph = [[] for _ in range(N+1)]

for _ in range(M):
    node1, node2 = list(map(int, input().split()))
    graph[node1].append(node2)
    graph[node2].append(node1)

queue = [1]
visit = [False for _ in range(N+1)]
answer = -1
while queue:
    node = queue.pop(0)

    if visit[node] is False:
        answer += 1
        visit[node] = True
        queue += graph[node]

print(answer)