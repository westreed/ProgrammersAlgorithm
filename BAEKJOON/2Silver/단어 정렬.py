# 문자열, 정렬
# https://www.acmicpc.net/problem/1181

num = int(input())
sets = set()
for _ in range(num):
    sets.add(input().rstrip())

lists = sorted(sets, key = lambda x:[len(x),x])
for l in lists:
    print(l)