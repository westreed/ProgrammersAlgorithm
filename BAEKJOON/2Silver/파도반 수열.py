# 수학, 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/9461

input = __import__('sys').stdin.readline
table = [0,1,1,1]
for i in range(3, 101):
        table.append(table[i-1]+table[i-2])

for _ in range(int(input())):
    print(table[int(input())])