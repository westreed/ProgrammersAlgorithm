# 자료구조, 세그먼트 트리
# https://www.acmicpc.net/problem/2357

import sys

def min_init(arr:list, tree:list, left_node:int, right_node:int, node:int=1):
    if left_node == right_node:
        tree[node] = arr[left_node]
        return tree[node]
    
    mid = (left_node+right_node)//2
    tree[node] = min(min_init(arr, tree, left_node, mid, node*2), min_init(arr, tree, mid+1, right_node, node*2+1))
    return tree[node]

def segment_min(tree:list, start:int, end:int, left_node:int, right_node:int, node:int=1):
    # 범위 밖인 경우
    if start > right_node or end < left_node:
        return 0xFFFFFFFF
    # 범위가 안쪽인 경우
    if left_node >= start and end >= right_node:
        return tree[node]
    
    mid = (left_node+right_node)//2
    m1 = segment_min(tree, start, end, left_node, mid, node*2)
    m2 = segment_min(tree, start, end, mid+1, right_node, node*2+1)
    return min(m1, m2)

def max_init(arr:list, tree:list, left_node:int, right_node:int, node:int=1):
    if left_node == right_node:
        tree[node] = arr[left_node]
        return tree[node]
    
    mid = (left_node+right_node)//2
    tree[node] = max(max_init(arr, tree, left_node, mid, node*2), max_init(arr, tree, mid+1, right_node, node*2+1))
    return tree[node]

def segment_max(tree:list, start:int, end:int, left_node:int, right_node:int, node:int=1):
    # 범위 밖인 경우
    if start > right_node or end < left_node:
        return -1
    # 범위가 안쪽인 경우
    if left_node >= start and end >= right_node:
        return tree[node]
    
    mid = (left_node+right_node)//2
    m1 = segment_max(tree, start, end, left_node, mid, node*2)
    m2 = segment_max(tree, start, end, mid+1, right_node, node*2+1)
    return max(m1, m2)


def solution1():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    min_tree = [0] * (len(arr)*4)
    max_tree = [0] * (len(arr)*4)

    min_init(arr, min_tree, 0, N-1)
    max_init(arr, max_tree, 0, N-1)

    output = []

    for _ in range(M):
        a, b = map(int, input().split())
        min_v = segment_min(min_tree, a-1, b-1, 0, N-1)
        max_v = segment_max(max_tree, a-1, b-1, 0, N-1)
        output.append(str(f"{min_v} {max_v}"))
    
    print("\n".join(output))

# solution1()

# =================================================================================
# 처음에 생각만 하고 넘어갔던 방법 (tree 하나에 tuple 쌍으로 (min, max) 저장)


# import sys

def init(arr:list, tree:list, left_node:int, right_node:int, node:int=1):
    if left_node == right_node:
        # 최소, 최대값이 원소 하나뿐이니 둘다 자기자신임
        tree[node] = (arr[left_node], arr[left_node])
        return tree[node]
    
    mid = (left_node+right_node)//2
    left = init(arr, tree, left_node, mid, node*2)
    right = init(arr, tree, mid+1, right_node, node*2+1)

    # min을 담을 땐 최소값끼리 중 더 최소를, max는 최대값끼리 비교
    tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
    return tree[node]

def get_segment(tree:list, start:int, end:int, left_node:int, right_node:int, node:int=1):
    # 범위 밖인 경우
    if start > right_node or end < left_node:
        return 0xFFFFFFFF, 0
    # 범위가 안쪽인 경우
    if left_node >= start and end >= right_node:
        return tree[node][0], tree[node][1]
    
    mid = (left_node+right_node)//2
    m1 = get_segment(tree, start, end, left_node, mid, node*2)
    m2 = get_segment(tree, start, end, mid+1, right_node, node*2+1)
    return min(m1[0], m2[0]), max(m1[1], m2[1])


def solution2():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    tree = [0] * (len(arr)*4)

    init(arr, tree, 0, N-1)
    output = []

    for _ in range(M):
        a, b = map(int, input().split())
        res = get_segment(tree, a-1, b-1, 0, N-1)
        output.append(str(f"{res[0]} {res[1]}"))
    
    print("\n".join(output))

solution2()