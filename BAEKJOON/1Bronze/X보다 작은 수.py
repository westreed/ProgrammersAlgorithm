# 수학, 구현
# https://www.acmicpc.net/problem/10871

length, number = map(int, input().split())
lists = list(map(int, input().split()))

result = ''
for i in range(length):
    if lists[i] < number:
        result += f'{lists[i]} '
print(result[:-1])