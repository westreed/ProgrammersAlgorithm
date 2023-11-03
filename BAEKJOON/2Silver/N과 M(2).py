# 
# https://www.acmicpc.net/problem/15650

N,M = map(int, input().split())

def bfs(start, cnt, res):
    global N, M
    if cnt == M:
        print(res)
    
    else:
        for i in range(start+1, N+1):
            bfs(i, cnt+1, f"{res} {i}")

for k in range(1, N-M+2):
    bfs(k, 1, str(k))