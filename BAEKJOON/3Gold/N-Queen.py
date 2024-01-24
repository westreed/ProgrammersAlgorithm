# 브루트포스 알고리즘, 백트래킹
# https://www.acmicpc.net/problem/9663

answer = 0

def can_position(x,y,vy):
    for idx in range(x):
        if vy[idx] == y: return False
        if abs(vy[idx]-y) == x-idx: return False
    
    return True

def dfs(N, x, vy):
    global answer
    if x == N:
        answer += 1
        return
    
    for y in range(N):
        if can_position(x,y,vy):
            vy[x] = y
            dfs(N, x+1, vy)
            vy[x] = -1


if __name__ == "__main__":
    N = int(input())

    # 퀸은 상하좌우, 대각선으로 무한하게 이동할 수 있다.
    # 한줄에 퀸은 최대 1마리만 배치가 가능하다.
    # NxN 크기의 보드에 N개의 퀸을 배치하려면, 한줄에 퀸을 하나씩 배치하는 경우의 수.
    # Pypy3로 제출해야 통과합니다.

    dfs(N, 0, vy=[-1 for _ in range(N)])
    print(answer)