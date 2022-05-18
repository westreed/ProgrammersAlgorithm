# 
# https://www.acmicpc.net/problem/2839

N = int(input())
maxv = float('inf')
lists = [maxv for _ in range(5001)]

lists[3] = 1
lists[5] = 1
for i in range(1,N+1):
    if i >= 3: lists[i] = min(lists[i], lists[i-3]+1)
    if i >= 5: lists[i] = min(lists[i], lists[i-5]+1)
    
print(lists[N] if lists[N] != maxv else -1)