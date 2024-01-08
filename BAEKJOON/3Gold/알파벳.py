# 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 백트래킹
# https://www.acmicpc.net/problem/1987

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    arrow = ((-1,0), (1,0), (0,-1), (0,1))
    R, C = map(int, input().split())
    maps = [
        list(map(lambda x: 1 << ord(x)-65, input().rstrip())) for _ in range(R)
    ]
    answer = 1

    def dfs(x, y, c, v):
        global answer
            
        for dx,dy in arrow:
            nx, ny = x+dx, y+dy

            if nx < 0 or nx >= R: continue
            if ny < 0 or ny >= C: continue

            _v = maps[nx][ny]

            if v & _v:
                if answer < c:
                    answer = c
            else:
                dfs(nx, ny, c+1, v | _v)
    
    dfs(0, 0, 1, maps[0][0])
    print(answer)