# 
# https://www.acmicpc.net/problem/11438

import sys
input = sys.stdin.readline

N = int(input())
tree = [0 for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
tree[1] = 1
depth[1] = 1

# 부모를 더 빠르게 찾을 수 있도록 해야할듯.
for _ in range(N-1):
    S, E = map(int, input().split())

    if tree[S]:
        tree[E] = S
        depth[E] = depth[S]+1

    else:
        tree[S] = E
        depth[S] = depth[E]+1

def findLCA(node1, node2):
    global tree, depth

    if depth[node1] > depth[node2]:
        while depth[node1] != depth[node2]:
            node1 = tree[node1]
    elif depth[node1] < depth[node2]:
        while depth[node1] != depth[node2]:
            node2 = tree[node2]
    
    if node1 == node2:
        return node1

    while tree[node1] != tree[node2]:
        node1 = tree[node1]
        node2 = tree[node2]
    
    return tree[node1]

M = int(input())
for _ in range(M):
    N1, N2 = map(int, input().split())
    sys.stdout.write(str(findLCA(N1, N2)) + "\n")