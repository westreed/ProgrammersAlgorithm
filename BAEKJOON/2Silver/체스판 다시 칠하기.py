# 브루트포스 알고리즘
# https://www.acmicpc.net/problem/1018

# M ㅣ  N ㅡ
M,N = map(int, input().split())
Chess = []
Check = ['BWBWBWBW','WBWBWBWB']

for m in range(M):
    data = input().strip()
    Chess.append(data)

sM, sN = M-7, N-7
Length = sM*sN
Answer = float('inf')

for m in range(sM):
    for n in range(sN):
        # m,n 은 시작점이고 8,8만큼 떨어진 좌표까지 출력
        checksum = [0,0]
        idx = 0
        for i in range(8):
            _temp = Chess[m+i][n:n+8]
            for j in range(2):
                ck = (idx+j) % 2
                for k in range(8):
                    if _temp[k] != Check[ck][k]:
                        checksum[j] += 1
            idx += 1
        result = min(checksum)
        if Answer > result:
            Answer = result

print(Answer)
