# 정렬
# https://www.acmicpc.net/problem/11650

# 입력
'''
5
3 4
1 1
1 -1
2 2
3 3
'''

input = __import__('sys').stdin.readline

Lists = [list(map(int, input().split())) for _ in range(int(input()))]
Lists.sort()

for l in Lists:
    print(*l)