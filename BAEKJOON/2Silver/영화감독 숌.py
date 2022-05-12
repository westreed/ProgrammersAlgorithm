# 브루트포스 알고리즘
# https://www.acmicpc.net/problem/1436

number = int(input())
start = 666
index = 1
while index <= number:
    if '666' in str(start):
        if number == index:
            print(str(start))
            break
        index += 1
    start += 1