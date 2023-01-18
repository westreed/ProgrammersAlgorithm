# 자료 구조, 트리를 사용한 집합과 맵, 우선순위 큐
# https://www.acmicpc.net/problem/7662

import heapq
input = __import__('sys').stdin.readline

class DualPriorityQueue:

    def __init__(self):
        self.length = 0
        self.MinHeap = []
        self.MaxHeap = []

    def insert(self, value):
        self.length += 1
        heapq.heappush(self.MinHeap, (value, -value))
        heapq.heappush(self.MaxHeap, (-value, value))
    
    def delete(self, type):
        if self.length:
            self.length -= 1

            if type == 1:
                value = heapq.heappop(self.MaxHeap)[1]
                for i in range(self.length, -1, -1):
                    if self.MinHeap[i][0] == value:
                        del self.MinHeap[i]
                        break
            
            elif type == -1:
                value = -heapq.heappop(self.MinHeap)[0]
                for i in range(self.length, -1, -1):
                    if self.MaxHeap[i][1] == value:
                        del self.MaxHeap[i]
                        break
    
    def print(self):
        if self.length > 1:
            print(self.MaxHeap[0][1])
            print(self.MinHeap[0][0])
        elif self.length == 1:
            print(self.MinHeap[0][0])
            print(self.MinHeap[0][0])
        else:
            print('EMPTY')


T = int(input())
for _ in range(T):
    N = int(input())
    Queue = DualPriorityQueue()

    for _ in range(N):
        Command, Value = input().split()
        if Command == 'I':
            Queue.insert(int(Value))
        elif Command == 'D':
            Queue.delete(int(Value))

    Queue.print()