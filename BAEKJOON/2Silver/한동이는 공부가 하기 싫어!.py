# 그래프 이론, 브루트포스 알고리즘, 그래프 탐색
# https://www.acmicpc.net/problem/3182

# 입력
'''
3
3
3
1

4
2
3
4
1

6
2
3
4
3
1
1

답
2
1
5
'''
input = __import__("sys").stdin.readline
N = int(input())
graph = [int(input()) for _ in range(N)]

def BFS(start):
    global N, graph
    queue = start
    visit = [False for _ in range(N)]
    count = -1
    while queue:
        node = queue-1
        if visit[node] is False:
            visit[node] = True
            count += 1
            queue = graph[node]
        else:
            break
    return (-count, start)

answer = []
for p in range(N):
    res = BFS(p+1)
    answer.append(res)

answer.sort()
print(answer[0][1])
