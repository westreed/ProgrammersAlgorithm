# 구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색
# https://www.acmicpc.net/problem/14502

"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""

arrow = ((-1,0),(1,0),(0,-1),(0,1))

def find_map(Maps,N,M,target):
    pairs = []
    for i in range(N):
        for j in range(M):
            if Maps[i][j] == target:
                pairs.append((i,j))
    return pairs

def count_virus(Maps,N,M,virus,case):
    from collections import deque
    visit = [[False for _ in range(M)] for _ in range(N)]
    queue = deque(virus)
    cnt = 0
    for cx, cy in case:
        Maps[cx][cy] = 3
    
    while queue:
        x,y = queue.popleft()
        cnt += 1
        for dx,dy in arrow:
            nx,ny = x+dx,y+dy
            if nx < 0 or nx >= N: continue
            if ny < 0 or ny >= M: continue
            if Maps[nx][ny] >= 1: continue # 1wall, 2virus, 3tempwall
            if visit[nx][ny] is True: continue
            visit[nx][ny] = True
            queue.append((nx,ny))
    
    for cx, cy in case:
        Maps[cx][cy] = 0

    return cnt
            
if __name__ == "__main__":
    from itertools import combinations
    input = __import__("sys").stdin.readline

    N, M = map(int, input().split())
    Maps = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    virus = find_map(Maps,N,M,2)
    empty = find_map(Maps,N,M,0)
    total_cnt = N*M
    base_wall_cnt = total_cnt-(len(virus)+len(empty))+3

    wall_cases = combinations(empty, 3)
    answer = 0
    for wall_case in wall_cases:
        virus_cnt = count_virus(Maps,N,M,virus,wall_case)
        # 전체갯수 - virus 갯수 - 벽갯수
        alive_cnt = total_cnt-virus_cnt-base_wall_cnt
        if answer < alive_cnt:
            answer = alive_cnt
    
    print(answer)
        