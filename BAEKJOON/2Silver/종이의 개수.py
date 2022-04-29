# 분할 정복, 재귀
# https://www.acmicpc.net/problem/1780

import sys
input = sys.stdin.readline

N = int(input())
Array = []
Count = {'-1':0,'0':0,'1':0}
for _ in range(N):
    Array.append(list(map(int, input().split())))

def paper(Array, N, X, Y):
    header = Array[Y][X]
    isSame = True
    for j in range(Y, Y+N):
        for i in range(X, X+N):
            if Array[j][i] != header:
                isSame = False
                break
        if isSame is False:
            break
    else:
        Count[str(header)] += 1
        return True
    
    size1 = int(N/3)
    size2 = size1*2
    paper(Array, size1, X, Y)
    paper(Array, size1, X+size1, Y)
    paper(Array, size1, X+size2, Y)
    paper(Array, size1, X, Y+size1)
    paper(Array, size1, X+size1, Y+size1)
    paper(Array, size1, X+size2, Y+size1)
    paper(Array, size1, X, Y+size2)
    paper(Array, size1, X+size1, Y+size2)
    paper(Array, size1, X+size2, Y+size2)
    return False

paper(Array, N, 0, 0)

for c in Count.values():
    print(c)