# 
# https://www.acmicpc.net/problem/10999

"""
5 2 2
1
2
3
4
5
1 3 4 6
2 2 5
1 1 3 -2
2 2 5
"""

# lazy segment tree 문제
# update를 매번 하지말고, 값이 필요할 때 밀린 업데이트를 처리하는 방법

def init(arr, tree, left, right, node=1):
    if left == right:
        tree[node] = arr[left]
        return tree[node]
    
    mid = (left+right)//2
    tree[node] = init(arr, tree, left, mid, node*2) + init(arr, tree, mid+1, right, node*2+1)
    return tree[node]

def push(tree, lazy, left, right, node):
    if lazy[node] == 0: return
    lazy_value = lazy[node]
    lazy[node] = 0

    tree[node] += (right-left+1)*lazy_value
    if left != right:
        lazy[node*2] += lazy_value
        lazy[node*2+1] += lazy_value


def update(tree, lazy, start, end, value, left, right, node=1):
    push(tree, lazy, left, right, node)
    if start > right or end < left:
        return
    
    if start <= left and right <= end:
        tree[node] += (right-left+1)*value
        if left != right: # not leaf node
            lazy[node*2] += value
            lazy[node*2+1] += value
        return
    
    mid = (left+right)//2
    update(tree, lazy, start, end, value, left, mid, node*2)
    update(tree, lazy, start, end, value, mid+1, right, node*2+1)
    tree[node] = tree[node*2] + tree[node*2+1]

def segment_sum(tree, lazy, start, end, left, right, node=1):
    push(tree, lazy, left, right, node)
    # 범위 밖인 경우
    if start > right or end < left:
        return 0
    # 범위가 안쪽인 경우
    if left >= start and end >= right:
        return tree[node]
    
    mid = (left+right)//2
    return segment_sum(tree, lazy, start, end, left, mid, node*2) + segment_sum(tree, lazy, start, end, mid+1, right, node*2+1)


if __name__ == "__main__":
    input = __import__("sys").stdin.readline
    N,M,K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    tree = [0] * (len(arr)*4)
    lazy = [0] * (len(arr)*4)

    init(arr, tree, 0, N-1)
    output = []
    for _ in range(M+K):
        cmd = list(map(int, input().split()))

        if cmd[0] == 1:
            update(tree, lazy, cmd[1]-1, cmd[2]-1, cmd[3], 0, N-1)
        elif cmd[0] == 2:
            res = segment_sum(tree, lazy, cmd[1]-1, cmd[2]-1, 0, N-1)
            output.append(str(res))
    
    print("\n".join(output))