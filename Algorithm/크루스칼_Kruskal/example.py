class UnionFind:

    def __init__(self, N):
        self.nodeList = [idx for idx in range(N+1)]

    def getRootNode(self, idx):
        if self.nodeList[idx] == idx:
            return idx

        else:
            self.nodeList[idx] = self.getRootNode(self.nodeList[idx])
            return self.nodeList[idx]

    def unionNode(self, idx1, idx2):
        node1 = self.getRootNode(idx1)
        node2 = self.getRootNode(idx2)

        if node1 > node2:
            self.nodeList[idx1] = node2
        else:
            self.nodeList[idx2] = node1

    def isConnectNode(self, idx1, idx2):
        node1 = self.getRootNode(idx1)
        node2 = self.getRootNode(idx2)

        if node1 == node2: return True
        return False
    
    def print(self):
        print(self.nodeList)

import heapq

class Kruskal:

    class Node:
        def __init__(self, n1, n2, v):
            self.node = (n1, n2)
            self.dist = v

        def __lt__(self, other):
            return self.dist < other.dist
        
        def __gt__(self, other):
            return self.dist > other.dist
    
    def __init__(self, n):
        self.n = n
        self.graph = []
    
    def push(self, n1, n2, v):
        heapq.heappush(self.graph, self.Node(n1, n2, v))

    def pop(self):
        return heapq.heappop(self.graph)

    def find(self):
        uf = UnionFind(self.n)
        totalDist = 0

        for _ in range(len(self.graph)):
            n = self.pop()
            if uf.isConnectNode(n.node[0], n.node[1]) is False:
                totalDist += n.dist
                uf.unionNode(n.node[0], n.node[1])
        
        print(totalDist)
    
    @staticmethod
    def printNode(node):
        print(f"node:{node.node} dist:{node.dist}")

if __name__ == "__main__":
    kr = Kruskal(7)
    kr.push(1,7,12)
    kr.push(1,4,28)
    kr.push(1,2,67)
    kr.push(1,5,17)
    kr.push(2,4,24)
    kr.push(2,5,62)
    kr.push(3,5,20)
    kr.push(3,6,37)
    kr.push(4,7,13)
    kr.push(5,6,45)
    kr.push(5,7,73)

    kr.printNode(kr.graph[0])
    kr.find()

