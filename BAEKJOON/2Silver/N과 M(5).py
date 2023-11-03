# 백트래킹
# https://www.acmicpc.net/problem/15652

N,M = map(int, input().split())
List = list(map(int, input().split()))
List.sort()

def bfs(start, vis, cnt, res):
    global N, M, List
    vis[start] = True

    if cnt == M:
        print(res)
    
    else:
        for i in range(N):
            if vis[i] is False:
                bfs(i, vis[:], cnt+1, f"{res} {List[i]}")

for k in range(N):
    vis = [False for _ in range(N)]
    bfs(k, vis, 1, str(List[k]))