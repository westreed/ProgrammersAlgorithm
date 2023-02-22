# 2023 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/150365


def solution(n, m, x, y, r, c, k):
    # 미로를 탈출 할 수 없는 경우는 최단거리경로의 가짓수를 뺀 나머지값이 홀수이면 불가능하다.
    minPath = abs(x-r)+abs(y-c)
    if (k-minPath) % 2 == 1: return "impossible"
    
    from collections import deque
    Queue = deque([(x,y,0,"")])
    direction = ((1, 0, "d"), (0, -1, "l"), (0, 1, "r"), (-1, 0, "u"))
    
    while Queue:
        cx,cy,cnt,path = Queue.popleft()
        
        if(cx,cy) == (r,c) and cnt == k:
            return path

        for dx,dy,dn in direction:
            nx, ny = cx+dx, cy+dy
            
            if abs(nx - r) + abs(ny - c) + cnt + 1 > k: continue
            if 1 <= nx <= n and 1 <= ny <= m:
                Queue.append((nx, ny, cnt+1, path+dn))
                break
                
    return "impossible"