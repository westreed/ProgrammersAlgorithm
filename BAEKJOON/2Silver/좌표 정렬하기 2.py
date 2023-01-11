# 정렬
# https://www.acmicpc.net/problem/11651

# 입력
'''
5
0 4
1 2
1 -1
2 2
3 3
'''

input = __import__('sys').stdin.readline
Lists = [list(map(int, input().split())) for _ in range(int(input()))]
Lists.sort(key=lambda x: (x[1], x[0]))

for l in Lists:
    print(*l)