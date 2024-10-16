# 그래프 이론, 그래프 탐색, 너비 우선 탐색
# https://www.acmicpc.net/problem/9205

"""
2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000

happy
sad
"""

input = __import__("sys").stdin.readline
t = int(input())

def length(a: tuple, b: tuple):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solution():
    n = int(input()) # store num
    node = []
    node.append(tuple(map(int, input().split())))
    for _ in range(n):
        node.append(tuple(map(int, input().split())))
    node.append(tuple(map(int, input().split())))

    n_ = n+2
    festival_id = n+1
    max_range = 20*50
    graph = [[] for _ in range(n_)]

    for i in range(n_):
        for j in range(n_):
            if i >= j or length(node[i], node[j]) > max_range:
                continue
            graph[i].append(j)
            graph[j].append(i)
    
    from collections import deque
    queue = deque([0])
    visit = [False] * n_

    while queue:
        node = queue.pop()
        visit[node] = True

        if node == festival_id:
            return "happy"
        
        for next in graph[node]:
            if visit[next]:
                continue
            queue.append(next)

    return "sad"

for _ in range(t):
   print(solution())