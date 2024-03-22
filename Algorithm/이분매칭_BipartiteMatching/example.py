N = 3
graph = {}
own = [-1] * N # 점유한 사람
chk = [False] * N # 점유여부


def dfs(x):
    for target in graph[x]:
        # 이미 체크된 target이면 스킵
        if chk[target]: continue
        chk[target] = True

        if own[target] == -1 or dfs(own[target]):
            own[target] = x
            return True
    return False

def reset_chk():
    global chk
    chk = [False]*N


if __name__ == "__main__":
    # 0은 0,1,2 중 아무거나 선택해도 됨.
    # 1은 0을 원함.
    # 2는 1을 원함.
    graph[0] = [0,1,2]
    graph[1] = [0]
    graph[2] = [1]

    count = 0

    for x in range(N):
        reset_chk()
        if dfs(x): count += 1
    
    print(count)
    for x, o in enumerate(own):
        print(f"{x} -> {o}")
