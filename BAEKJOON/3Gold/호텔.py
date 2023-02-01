# 다이나믹 프로그래밍, 배낭 문제
# https://www.acmicpc.net/problem/1106

input = __import__('sys').stdin.readline
C, N = map(int, input().split())
Cost = [list(map(int, input().split())) for _ in range(N)]
DP = [100000 for _ in range(C+100)]
DP[0] = 0

for n in range(N):
    cost, num = Cost[n]
    for p in range(num, C+100):
        DP[p] = min(DP[p-num]+cost, DP[p])

print(min(DP[C:]))


# import heapq, math
# input = __import__('sys').stdin.readline
# C, N = map(int, input().split())
# Cost = []

# for _ in range(N): # O(N)
#     cost, num = map(int, input().split())
#     Cost.append([-num/cost, cost, num])

# print(Cost)

# heapq.heapify(Cost) # O(N)
# _, cost, num = Cost[0] # 가장 효율이 좋음
# P, C = divmod(C, num)
# Money = P*cost

# min_cost = 0xFFFFFFFF
# for i in range(N):
#     _, cost, num = Cost[i]
#     cost = math.ceil(C/num) * cost
#     if min_cost > cost:
#         min_cost = cost

# Money += min_cost
# print(Money)