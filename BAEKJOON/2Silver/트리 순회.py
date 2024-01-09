# 
# https://www.acmicpc.net/problem/1991

def preorder(start, graph):
    if start == '.': return
    yield start
    yield from preorder(graph[start][0], graph)
    yield from preorder(graph[start][1], graph)

def inorder(start, graph):
    if start == '.': return
    yield from inorder(graph[start][0], graph)
    yield start
    yield from inorder(graph[start][1], graph)

def postorder(start, graph):
    if start == '.': return
    yield from postorder(graph[start][0], graph)
    yield from postorder(graph[start][1], graph)
    yield start

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline
    N = int(input())
    graph = {}

    for _ in range(N):
        a, *b = input().split()
        graph[a] = b
    
    for res in preorder('A', graph):
        print(res, end="")
    print()
    for res in inorder('A', graph):
        print(res, end="")
    print()
    for res in postorder('A', graph):
        print(res, end="")