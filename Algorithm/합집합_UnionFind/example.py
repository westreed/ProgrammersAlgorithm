
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


if __name__ == "__main__":
    graph = UnionFind(8)
    graph.unionNode(1, 2)
    graph.unionNode(2, 3)
    graph.unionNode(3, 4)
    graph.unionNode(5, 6)
    graph.unionNode(6, 7)
    graph.unionNode(7, 8)
    graph.print()

    print(f"1과 5는 연결되어있는가? {graph.isConnectNode(1, 5)}")
    graph.unionNode(1, 5)
    graph.print()
    print(f"1과 5는 연결되어있는가? {graph.isConnectNode(1, 5)}")
    print(f"3과 6는 연결되어있는가? {graph.isConnectNode(3, 6)}")
    graph.print()