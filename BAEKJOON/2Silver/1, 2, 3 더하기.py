# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/9095

from collections import deque
input = __import__('sys').stdin.readline
T = int(input())

# ver 1 (BFS)
def ver1(N):
    A = 0
    Queue = deque([1,2,3])
    while Queue:
        n = Queue.pop()

        if n == N: A += 1
        if n >= N: continue

        for i in range(1,4):
            Queue.append(n+i)

    print(A)

# ver 2 (DP)
def ver2(N):
    A = 0
    D = [0 for _ in range(11)]
    D[0] = 1
    D[1] = 1
    D[2] = 2

    for i in range(3, N+1):
        D[i] = D[i-1]+D[i-2]+D[i-3]
    
    print(D[N])

for _ in range(T):
    N = int(input())
    
    ver1(N)
    ver2(N)