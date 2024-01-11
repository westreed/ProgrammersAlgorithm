# 그래프 이론, 그래프 탐색, 트리, 재귀
# https://www.acmicpc.net/problem/5639

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root:Node):
        self.root = root
    
    def add(self, node:Node):
        target = self.root

        while True:
            if target.data > node.data:
                if target.left is None:
                    target.left = node
                    return True
                else:
                    target = target.left
            else:
                if target.right is None:
                    target.right = node
                    return True
                else:
                    target = target.right
    
    def _preorder(self, target:Node):
        if target is None: return
        print(target.data)
        self._preorder(target.left)
        self._preorder(target.right)

    def preorder(self):
        self._preorder(self.root)
    
    def _postorder(self, target:Node):
        if target is None: return
        self._postorder(target.left)
        self._postorder(target.right)
        print(target.data)
    
    def postorder(self):
        self._postorder(self.root)

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(1000000)

    input = sys.stdin.read().split()
    tree = BinaryTree(Node(int(input.pop(0))))

    while input:
        node = Node(int(input.pop(0)))
        tree.add(node)
    
    tree.postorder()