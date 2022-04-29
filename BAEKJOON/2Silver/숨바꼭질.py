# 그래프 탐색, BFS
# https://www.acmicpc.net/problem/1697

def move(N, K):
    from collections import deque

    queue = deque()
    queue.append(N)
    visit = [0 for _ in range(100002)]

    while queue:
        pos = queue.popleft()

        if pos == K:
            print(visit[pos])
            break
        
        for next in (pos+1, pos-1, pos*2):
            if 0 <= next <= 100001 and visit[next] == 0:
                visit[next] = visit[pos]+1
                queue.append(next)
    

N, K = map(int, input().split())
if N == K: print(0)
elif N > K: print(N-K)
else: move(N, K)