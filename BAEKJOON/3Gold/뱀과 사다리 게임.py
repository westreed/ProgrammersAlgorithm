# 그래프 이론, 그래프 탐색, 너비 우선 탐색
# https://www.acmicpc.net/problem/16928

input = __import__("sys").stdin.readline
N, M = map(int, input().split())

board = [0 for _ in range(101)]
visit = [0 for _ in range(101)]

for _ in range(N+M):
    a, b = map(int, input().split())
    board[a] = b

from collections import deque
queue = deque([1]) # 1번 칸부터 시작

while queue:
    node = queue.popleft()
    if node == 100: break

    for dice in range(1, 7):
        nxt = node+dice

        if nxt > 100 or visit[nxt]:
            continue

        visit[nxt] = visit[node]+1
        if board[nxt]:
            nxt = board[nxt]
            if visit[nxt]:
                continue
            visit[nxt] = visit[node]+1
        queue.append(nxt)

print(visit[100])