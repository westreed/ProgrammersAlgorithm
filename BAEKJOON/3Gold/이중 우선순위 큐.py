# 자료 구조, 트리를 사용한 집합과 맵, 우선순위 큐
# https://www.acmicpc.net/problem/7662

import heapq
input = __import__('sys').stdin.readline

class DualPriorityQueue:

    def __init__(self, N):
        self.MinHeap = []
        self.MaxHeap = []
        self.State = [False] * N

    def insert(self, value, idx):
        heapq.heappush(self.MinHeap, (value, idx))
        heapq.heappush(self.MaxHeap, (-value, idx))
        self.State[idx] = True
    
    def setup(self, heap):
        while heap and not self.State[heap[0][1]]:
            heapq.heappop(heap)
    
    def pop(self, heap):
        self.setup(heap)
        if heap:
            self.State[heap[0][1]] = False
            heapq.heappop(heap)

    
    def delete(self, type):
        if type == 1:       self.pop(self.MaxHeap)
        elif type == -1:    self.pop(self.MinHeap)
    
    def print(self):
        self.setup(self.MaxHeap)
        self.setup(self.MinHeap)
        if self.MaxHeap:    print(-self.MaxHeap[0][0], self.MinHeap[0][0])
        else:               print('EMPTY')


T = int(input())
for _ in range(T):
    N = int(input())
    Queue = DualPriorityQueue(N)

    for idx in range(N):
        Command, Value = input().split()
        if Command == 'I':
            Queue.insert(int(Value), idx)
        elif Command == 'D':
            Queue.delete(int(Value))

    Queue.print()