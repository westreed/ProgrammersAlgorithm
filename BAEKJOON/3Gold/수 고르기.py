# 
# https://www.acmicpc.net/problem/2230

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()

end = 0
ans = nums[N-1]-nums[0]

for start in range(N):
    while end < N:
        diff = nums[end]-nums[start]
        if diff >= M:
            ans = min(ans, diff)
            break
        else:
            end += 1

print(ans)

