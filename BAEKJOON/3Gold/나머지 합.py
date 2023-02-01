# 수학, 누적 합
# https://www.acmicpc.net/problem/10986

# 입력
'''
5 3
1 2 3 1 2
'''

N, M = map(int, input().split())
List = list(map(int, input().split()))

for idx in range(1, N):
    List[idx] += List[idx-1]

Left = __import__('collections').defaultdict(int)

for idx in range(N):
    Left[List[idx]%M] += 1

Answer = Left[0]
for k in Left:
    n = Left[k]
    if n > 1:
        Answer += (n*(n-1))//2

print(Answer)