# 
# https://www.acmicpc.net/problem/9465

if __name__ == "__main__":
    import sys, heapq
    input = sys.stdin.readline
    T = int(input())
    arrow = ((-1,0),(1,0),(0,-1),(0,1))

    for _ in range(T):
        N = int(input())
        stikers = [list(map(int, input().split())) for _ in range(2)]
        caches = []

        for x in range(2):
            for y in range(N):
                score = stikers[x][y]
                for dx,dy in arrow:
                    nx,ny = x+dx, y+dy
                    if nx < 0 or nx >= 2: continue
                    if ny < 0 or ny >= N: continue
                    score -= stikers[nx][ny]

                heapq.heappush(caches, (-score, x, y))
        
        total = 0
        while caches:
            _, x, y = heapq.heappop(caches)
            if stikers[x][y]:
                total += stikers[x][y]
                for dx,dy in arrow:
                    nx,ny = x+dx, y+dy
                    if nx < 0 or nx >= 2: continue
                    if ny < 0 or ny >= N: continue
                    stikers[nx][ny] = 0
        
        print(total)