#
# https://www.acmicpc.net/problem/1018
from math import ceil

M,N = map(int, input().split())
Chess = []
Pattern = []
Checksum = []
for m in range(M):
    data = input().strip()
    Chess.append(data)

data = 'BW' * ceil(N/2)
Pattern.append(data[:N])
data = 'WB' * ceil(N/2)
Pattern.append(data[:N])

for i in range(2):
    

for m in range(M):
    pass