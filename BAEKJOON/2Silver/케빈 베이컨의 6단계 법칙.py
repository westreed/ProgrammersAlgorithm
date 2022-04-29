# BFS, 플로이드–와샬
# https://www.acmicpc.net/problem/1389

# 입력
'''
5 5
1 3
1 4
4 5
4 3
3 2

5 4
1 2
2 3
3 4
4 5
'''
from collections import defaultdict
N, M = map(int, input().split())
Friends = defaultdict(set)

for _ in range(M):
    A, B = map(int, input().split())
    Friends[A].add(B)
    Friends[B].add(A)

def find(A, B):
    from collections import deque

    queue = deque()
    queue.append([A, 0])
    visit = [False for _ in range(N+1)]
    visit[A] = True
    result = 0

    while queue:
        target, cnt = queue.popleft()

        if target == B:
            result = cnt
            break
            
        for k in Friends[target]:
            if visit[k] is False:
                visit[k] = True
                queue.append([k, cnt+1])

    return result

kebin = []
for a in range(1,N+1):
    total = 0
    for b in range(1, N+1):
        if a != b: total += find(a, b)
    kebin.append([total, a])

print(min(kebin)[1])