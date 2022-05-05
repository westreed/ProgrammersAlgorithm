# 수학, 구현, 사칙연산
# https://www.acmicpc.net/problem/2577

from collections import OrderedDict

value = 1
for _ in range(3):
    value *= int(input())

value = str(value)
dicts = OrderedDict([(str(key), 0) for key in range(10)])
for v in value:
    dicts[v] += 1

for d in dicts.values():
    print(d)