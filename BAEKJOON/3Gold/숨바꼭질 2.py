# 그래프 이론, 그래프 탐색, 너비 우선 탐색ㄷ
# https://www.acmicpc.net/problem/12851

if __name__ == "__main__":
    from collections import deque
    N, K = map(int, input().split())
    INF = 0xFFFFFFFF
    SIZE = 100001

    MAX = min(SIZE, K*2)
    dist = [INF] * 100001
    dist[N] = 0
    queue = deque([N])
    answer = []
    flag = False

    while queue:
        X = queue.popleft()

        if X == K:
            answer.append(dist[X])
            flag = True
            continue
        
        X2 = X*2
        cost = dist[X]+1

        if flag is True and answer[0] < cost:
            continue

        if X2 <= MAX and dist[X2] >= cost:
            dist[X2] = cost
            queue.append(X2)

        if X > 0 and dist[X-1] >= cost:
            dist[X-1] = cost
            queue.append(X-1)
        
        if X <= MAX and dist[X+1] >= cost:
            dist[X+1] = cost
            queue.append(X+1)
    
    print(answer[0])
    print(len(answer))