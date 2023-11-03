# 백트래킹
# https://www.acmicpc.net/problem/15652

N,M = map(int, input().split())
List = list(map(int, input().split()))
List.sort()

def bfs(start, cnt, res):
    global N, M, List

    if cnt == M:
        print(res)
    
    else:
        for i in range(start, N):
            bfs(i, cnt+1, f"{res} {List[i]}")

for k in range(N):
    bfs(k, 1, str(List[k]))