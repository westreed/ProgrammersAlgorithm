# 
# https://www.acmicpc.net/problem/9375

from collections import defaultdict
from functools import reduce
input = __import__('sys').stdin.readline
T = int(input())

# 전략
# 각 종류의 옷에 "안입음"을 의미하는 상태를 하나 더 넣어서,
# 전체경우수 - 1 = 최소 1개이상 입은 상태로 계산함.

for _ in range(T):
    N = int(input())
    if N == 0:
        print(0)
        continue

    Cloths = defaultdict(int)
    for _ in range(N):
        _, types = input().split()
        Cloths[types] += 1
    
    # "안입음" 상태 추가하기
    for types in Cloths:
        Cloths[types] += 1
    
    print(reduce(lambda a,b : a*b, list(Cloths.values()))-1)
    