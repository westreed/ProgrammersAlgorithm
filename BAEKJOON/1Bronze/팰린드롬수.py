# 구현, 문자열
# https://www.acmicpc.net/problem/1259

import sys
input = sys.stdin.readline

while True:
    case = input().rstrip()
    if case == '0': break

    reverse = case[::-1]
    if case == reverse:
        print('yes')
    else:
        print('no')