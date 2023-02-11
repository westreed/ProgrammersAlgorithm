# 수학, 정수론, 유클리드 호제법
# https://www.acmicpc.net/problem/2609

from functools import reduce

A,B = map(int, input().split())
cnt = 2
divisior = [1]
while cnt <= A and cnt <= B:
    if A % cnt == 0 and B % cnt == 0:
        A //= cnt
        B //= cnt
        divisior.append(cnt)
    cnt += 1

# def multi(a, b):
#     return a * b

print(reduce(lambda a,b : a*b, divisior))
print(reduce(lambda a,b : a*b, divisior+[A,B]))