# 구현, 문자열
# https://www.acmicpc.net/problem/2675

import sys
input = sys.stdin.readline

case = int(input())
for c in range(case):
    cnt, string = input().split()
    cnt, answer = int(cnt), ''

    for s in string:
        answer += s*cnt

    print(answer)