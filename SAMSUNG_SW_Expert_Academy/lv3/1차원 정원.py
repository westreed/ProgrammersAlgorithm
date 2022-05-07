# 14178
# 연습문제

'''
3
5 1
5 2
100 3
'''

import math

case = int(input())
answer = ''

for c in range(case):
    N,D = map(int, input().split())
    D = D*2 + 1
    cnt = math.ceil(N / D)
    answer += f'#{c+1} {cnt}\n'

print(answer)