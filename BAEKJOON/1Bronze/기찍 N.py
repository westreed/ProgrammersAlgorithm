# 구현
# https://www.acmicpc.net/problem/2742

num = int(input())
result = ''
for i in range(num, 0, -1):
    result += f'{i}\n'
print(result)