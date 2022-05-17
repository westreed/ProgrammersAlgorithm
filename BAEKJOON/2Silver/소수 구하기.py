# 수학, 정수론, 소수판정, 에라토스테네스의 체
# https://www.acmicpc.net/problem/1929

M,N = map(int, input().split())
Max = 1000000
Table = [i for i in range(Max+1)]

Table[1] = 0
for k in range(2,Max):
    if Table[k]:
        idx = 2*k
        while idx <= Max:
            Table[idx] = 0
            idx += k

for j in range(M,N+1):
    if Table[j]:
        print(Table[j])