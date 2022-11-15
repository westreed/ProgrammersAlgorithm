# 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 플로이드-워셜
# https://www.acmicpc.net/problem/1058

# 입력
'''
5
NYNNN
YNYNN
NYNYN
NNYNY
NNNYN

10
NNNNYNNNNN
NNNNYNYYNN
NNNYYYNNNN
NNYNNNNNNN
YYYNNNNNNY
NNYNNNNNYN
NYNNNNNYNN
NYNNNNYNNN
NNNNNYNNNN
NNNNYNNNNN

15
NNNNNNNNNNNNNNY
NNNNNNNNNNNNNNN
NNNNNNNYNNNNNNN
NNNNNNNYNNNNNNY
NNNNNNNNNNNNNNY
NNNNNNNNYNNNNNN
NNNNNNNNNNNNNNN
NNYYNNNNNNNNNNN
NNNNNYNNNNNYNNN
NNNNNNNNNNNNNNY
NNNNNNNNNNNNNNN
NNNNNNNNYNNNNNN
NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
YNNYYNNNNYNNNNN

정답
4
8
6
'''

import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    res = input().strip()
    for j in range(N):
        if res[j] == 'Y':
            graph[i].append(j)

def BFS(start):
    global N, graph

    answer = 0
    queue = []
    visit = [False for _ in range(N)]
    visit[start] = True
    for nxt in graph[start]:
        queue.append((0, nxt))

    while queue:
        cnt, node = queue.pop(0)
        if visit[node] is False:
            visit[node] = True
            if cnt < 2:
                answer += 1
                for nxt in graph[node]:
                    queue.append((cnt+1, nxt))
    
    return answer

friends = 0
for i in range(N):
    res = BFS(i)
    if friends < res:
        friends = res

print(friends)