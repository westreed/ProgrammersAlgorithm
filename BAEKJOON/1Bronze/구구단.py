# 수학, 구현, 사칙연산
# https://www.acmicpc.net/problem/2739

num = int(input())
result = ''
for i in range(1,10):
    result += f'{num} * {i} = {num*i}\n'
print(result)