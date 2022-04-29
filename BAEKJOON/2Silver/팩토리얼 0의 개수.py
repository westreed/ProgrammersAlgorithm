# 수학, 임의 정밀도 / 큰 수 연산
# https://www.acmicpc.net/problem/1676

import math

num = int(input())
res = list(str(math.factorial(num)))
cnt = 0

while True:
    pop = res.pop()
    if pop == '0': cnt += 1
    else: break

print(cnt)