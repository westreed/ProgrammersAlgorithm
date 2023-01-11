# 구현, 자료 구조, 큐
# https://www.acmicpc.net/problem/11866

N, K = map(int, input().split())

Lists = [i+1 for i in range(N)]
Index = 0
Length = N

Res = '<'
for _ in range(N):
    Index += K-1
    if Index >= Length: Index %= Length

    if Length > 1: Res += f'{Lists[Index]}, '
    else: Res += f'{Lists[Index]}>'
    del Lists[Index]
    Length -= 1

print(Res)