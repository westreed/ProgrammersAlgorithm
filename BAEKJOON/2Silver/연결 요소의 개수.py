# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# https://www.acmicpc.net/problem/11724

class Union_Find:
    def __init__(self, N):
        self.Size = N
        self.Node = [n for n in range(N+1)]

    def get(self, x):
        if self.Node[x] != x:
            self.Node[x] = self.get(self.Node[x])
            return self.Node[x]
        return x

    def union(self, u, v):
        u = self.get(u)
        v = self.get(v)

        if u < v: self.Node[v] = u
        else: self.Node[u] = v
    
    def find(self):
        cc = 0
        for i in range(1, self.Size+1):
            if self.Node[i] == i:
                cc += 1
        
        print(cc)

input = __import__('sys').stdin.readline
N, M = map(int, input().split())
Root = Union_Find(N)

for _ in range(M):
    u, v = map(int, input().split())
    Root.union(u, v)

Root.find()