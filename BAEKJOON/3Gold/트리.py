# 자료 구조, 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색, 분리 집합
# https://www.acmicpc.net/problem/4803

import sys
from collections import deque

input = sys.stdin.readline

def dfs(start, graph, visit):
    stack = deque([(start)])
    is_not_cycle = True
    while stack:
        node = stack.pop()
        if visit[node]:
            is_not_cycle = False
            continue
        
        visit[node] = True

        for nxt in graph[node]:
            if not visit[nxt]:
                stack.append((nxt))
    
    return is_not_cycle

tc = 0
tc_answer = []
while True:
    N,M = map(int, input().split())
    if N == M == 0:
        break

    tc += 1
    visit = [False]*(N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = 0
    for n in range(1, N+1):
        if not visit[n] and dfs(n, graph, visit):
            answer += 1
    
    print_answer = f"Case {tc}: "
    if answer == 0:
        print_answer += "No trees."
    elif answer == 1:
        print_answer += "There is one tree."
    else:
        print_answer += f"A forest of {answer} trees."
    
    tc_answer.append(print_answer)

print("\n".join(tc_answer))