# 수학, 사칙연산
# https://www.acmicpc.net/problem/3052

lists = {}
for i in range(10):
    value = int(input())
    lists[value%42] = 1
print(len(lists))