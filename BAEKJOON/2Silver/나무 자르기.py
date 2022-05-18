# 이분탐색, 매개변수탐색
# https://www.acmicpc.net/problem/2805

N,M = map(int, input().split())
Trees = list(map(int, input().split()))

def Cutting(Height):
    Total = 0
    for T in Trees:
        if T > Height:
            Total += T-Height
    return Total

start, ends = 0, max(Trees)
Answer = 0
while start <= ends:
    mid = (start+ends)//2
    Cut = Cutting(mid)
    if Cut >= M:
        Answer = max(Answer, mid)
        start = mid+1
    else:
        ends = mid-1
print(Answer)