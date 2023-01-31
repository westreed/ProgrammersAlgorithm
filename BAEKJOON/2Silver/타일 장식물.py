# 수학, 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/13301

def circumference(N):
    if N == 1: return 4
    Table = [1 for _ in range(81)]

    for i in range(3, N+1):
        Table[i] = Table[i-1] + Table[i-2]

    return (Table[N]*2+Table[N-1])*2

print(circumference(int(input())))