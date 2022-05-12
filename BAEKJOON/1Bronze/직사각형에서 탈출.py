# 수학, 기하학
# https://www.acmicpc.net/problem/1085

x,y,w,h = map(int, input().split())
result = min(x, y, abs(x-w), abs(y-h))
print(result)