# 2021 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/72413

INF = 0xFFFFFFFF

def dijkstra(graph, n, start):
    import heapq
    dist = [INF] * (n+1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]: continue

        for next_node, next_cost in graph[node]:
            # start에서 node까지의 비용 + next_node의 비용
            sum_cost = dist[node] + next_cost

            # 합한 비용이 next_node까지의 최소비용보다 큰 경우
            if dist[next_node] <= sum_cost:
                continue
            
            dist[next_node] = sum_cost
            heapq.heappush(heap, (sum_cost, next_node))
    
    return dist


def solution(n, s, a, b, fares):
    from collections import defaultdict
    graph = defaultdict(list)

    for fare in fares:
        i,j,cost = fare
        graph[i].append((j,cost))
        graph[j].append((i,cost))

    # A-X, B-X, S-X 사이의 거리가 최소가 되는 지점을 찾아야 한다.
    min_dist = INF
    for x in range(1, n+1):
        dist = dijkstra(graph, n, x)
        sum_dist = dist[a]+dist[b]+dist[s]
        if min_dist > sum_dist:
            min_dist = sum_dist
    
    return min_dist
            

n = [6,7,6]
s = [4,3,4]
a = [6,4,5]
b = [2,1,6]
fares = [
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
    [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
    [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
]
result = [82, 14, 18]

for q in [0,1,2]:
    qid = solution(n[q], s[q], a[q], b[q], fares[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')