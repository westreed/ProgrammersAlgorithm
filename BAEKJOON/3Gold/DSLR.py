# 
# https://www.acmicpc.net/problem/9019

from collections import deque

def D(n):
    return (n*2) % 10000

def S(n):
    if n == 0: return 9999
    else: return n-1

def L(n):
    a,b = divmod(n, 1000)
    return b*10 + a

def R(n):
    a,b = divmod(n, 10)
    return b*1000 + a

Trg = {
    "D": lambda x: D(x),
    "S": lambda x: S(x),
    "L": lambda x: L(x),
    "R": lambda x: R(x)
}

input = __import__('sys').stdin.readline
T = int(input())

for _ in range(T):
    A,B = map(int, input().split())
    Visit = [False for _ in range(10000)]

    Visit[A] = True
    Queue = deque([[A, ""]])
    while True:
        N,V = Queue.popleft()
        
        if N == B:
            print(V)
            break

        for _C in ['D','S','L','R']:
            _N = Trg[_C](N)
            if not Visit[_N]:
                Visit[_N] = True
                Queue.append([_N, V+_C])