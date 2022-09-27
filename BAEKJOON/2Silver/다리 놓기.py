# 수학, 다이나믹 프로그래밍, 조합론
# https://www.acmicpc.net/problem/1010

'''
3
2 2
1 5
13 29
'''

from math import comb
num = int(input())
ans = ''

def max_(a,b):
    if a > b: return a,b
    return b,a

for i in range(num):
    a,b = list(map(int, input().split()))
    a,b = max_(a,b)
    ans += str(comb(a,b))+'\n'

print(ans)