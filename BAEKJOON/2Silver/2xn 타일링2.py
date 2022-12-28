# 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/11727

# 입력
'''
2
'''

input = __import__("sys").stdin.readline
N = int(input())

A = [0, 1, 3, 5]
for i in range(4, N+1):
    A.append(A[i-1] + 2*A[i-2])

print(A[N] % 10007)