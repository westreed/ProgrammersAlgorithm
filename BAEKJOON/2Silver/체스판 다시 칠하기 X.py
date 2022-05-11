#
# https://www.acmicpc.net/problem/1018

# M ㅣ  N ㅡ
M,N = map(int, input().split())
Chess = []
for m in range(M):
    data = input().strip()
    Chess.append(data)

sM, sN = M-7, N-7
Length = sM*sN

for n in range(sN):
    for m in range(sM):
        