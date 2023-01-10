# 자료구조, 정렬, 이분탐색, 해시를 사용한 집합과 맵
# https://www.acmicpc.net/problem/10816

# 입력
'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
'''
from collections import defaultdict
input = __import__('sys').stdin.readline

N = int(input())
NumberCards = defaultdict(int)
for number in map(int, input().split()):
    NumberCards[number] += 1

M = int(input())
for number in map(int, input().split()):
    print(f'{NumberCards[number]}', end=' ')
    