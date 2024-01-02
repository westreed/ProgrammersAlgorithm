# [PCCP 기출문제] 2번
# https://school.programmers.co.kr/learn/courses/30/lessons/250136

def bfs(n, m, N, M, land):
    from collections import deque

    count = 1
    land[n][m] = 2
    col = set([m])
    queue = deque()
    queue.append((n,m))

    while queue:
        _n, _m = queue.popleft()
        for an, am in ((-1,0),(1,0),(0,-1),(0,1)):
            next_n = _n+an
            next_m = _m+am

            if next_n < 0 or next_n >= N: continue
            if next_m < 0 or next_m >= M: continue
            if land[next_n][next_m] != 1: continue
            count += 1
            land[next_n][next_m] = 2
            col.add(next_m)
            queue.append((next_n, next_m))
    
    # 석유 덩어리, 해당 덩어리가 속한 가로 위치
    return count, col

def solution(land):
    from collections import defaultdict
    # N 세로길이, M 가로길이
    N, M = len(land), len(land[0])
    col_chunk = defaultdict(int) # 가로좌표에 해당하는 석유 덩어리 크기

    for n in range(N):
        for m in range(M):
            if land[n][m] == 1:
                chunk_cnt, col_grid = bfs(n,m,N,M,land)
                for col in col_grid:
                    col_chunk[col] += chunk_cnt

    return max(col_chunk.values())


land = [
    [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]],
    [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
]

result = [
    9,
    16
]

for q in [0,1]:
    qid = solution(land[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')