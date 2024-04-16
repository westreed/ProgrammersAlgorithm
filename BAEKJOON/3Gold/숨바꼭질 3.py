# 
# https://www.acmicpc.net/problem/13549

"""
5 17
"""

# X기준 걷기 > 1s X-1 or X+1
# X기준 순간이동 > 0s 2X

# 5 > 10 ? 5 > 6 > 12 ? 5 > 6> 7 > 14 
# 10 > 20 ? 10 > 9 > 18
# 

def HideAndSeek():
    import heapq
    N, K = map(int, input().split())
    if N > K:
        print(N-K)
        return
    
    _INF = 0xFFFFFFFF
    _MAX = 200001
    _RNG = K*2
    dist = [_INF] * _MAX
    dist[N] = 0

    heap = [(0, N)]
    while heap:
        _dist, node = heapq.heappop(heap)
        if _dist > dist[node]: continue

        for _cost, _move in ((0, 2), (1, -1), (1, 1)):
            _node = node*2 if _move == 2 else node+_move
            if _node < 0 or _node >= _RNG: continue

            sum_cost = dist[node] + _cost
            if sum_cost >= dist[_node]: continue
            dist[_node] = sum_cost
            heapq.heappush(heap, (sum_cost, _node))
    
    print(dist[K])


if __name__ == "__main__":
    HideAndSeek()
