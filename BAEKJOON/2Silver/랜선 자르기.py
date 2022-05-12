# 이분 탐색, 매개 변수 탐색
# https://www.acmicpc.net/problem/1654

'''
2 2
1
2147483647

1073741823

4 4
100
100
100
100

1 1
2147483647
'''
K,N = map(int, input().split())
lists = []
for _ in range(K):
    lists.append(int(input()))

start = 1
ends = max(lists)
answer = 0
while start <= ends:
    mid = (start+ends)//2
    total = 0
    for l in lists:
        total += l // mid

    if total >= N:
        start = mid+1
        answer = max(answer, mid)

    elif total < N: ends = mid-1

print(answer)