# 자료 구조, 해시를 사용한 집합과 맵
# https://www.acmicpc.net/problem/17219

input = __import__("sys").stdin.readline
N, M = map(int, input().split())

Memo = {}
for _ in range(N):
    address, password = input().split()
    Memo[address] = password

for _ in range(M):
    address = input().rstrip()
    print(Memo[address])