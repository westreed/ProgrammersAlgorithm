# 자료 구조, 세그먼트 트리
# https://www.acmicpc.net/problem/2042

"""
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
"""
import sys

def init(arr:list, tree:list, left_node:int, right_node:int, node:int=1):
    if left_node == right_node:
        tree[node] = arr[left_node]
        return tree[node]
    
    mid = (left_node+right_node)//2
    tree[node] = init(arr, tree, left_node, mid, node*2) + init(arr, tree, mid+1, right_node, node*2+1)
    return tree[node]

def segment_sum(tree:list, start:int, end:int, left_node:int, right_node:int, node:int=1):
    # 범위 밖인 경우
    if start > right_node or end < left_node:
        return 0
    # 범위가 안쪽인 경우
    if left_node >= start and end >= right_node:
        return tree[node]
    
    mid = (left_node+right_node)//2
    return segment_sum(tree, start, end, left_node, mid, node*2) + segment_sum(tree, start, end, mid+1, right_node, node*2+1)

def update(tree:list, index:int, value:int, left_node:int, right_node:int, node:int=1):
    if left_node > index or right_node < index:
        return
    
    tree[node] += value # value는 변화량임
    if left_node == right_node:
        return
    
    mid = (left_node+right_node)//2
    update(tree, index, value, left_node, mid, node*2)
    update(tree, index, value, mid+1, right_node, node*2+1)


if __name__ == "__main__":
    input = sys.stdin.readline
    N,M,K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    tree = [0] * (len(arr)*4)

    init(arr, tree, 0, N-1)
    
    output = []
    for _ in range(M+K):
        a,b,c = map(int, input().split())

        if a == 1:
            idx = b-1
            update(tree, idx, c-arr[idx], 0, N-1)
            arr[idx] = c
        
        elif a == 2:
            res = segment_sum(tree, b-1, c-1, 0, N-1)
            output.append(str(res))
    
    print("\n".join(output))