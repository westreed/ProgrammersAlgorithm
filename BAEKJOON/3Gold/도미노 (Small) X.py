# 
# https://www.acmicpc.net/problem/14586

# 예제
'''
4
1 3
2 1
3 1
5 5
답 1

7
1 1
2 1
3 1
5 5
6 7
8 1
10 1
답 2
'''

input = __import__('sys').stdin.readline
N = int(input())
position, height = [0 for _ in range(N)], [0 for _ in range(N)]

for i in range(N):
    pos, hei = map(int, input().split())
    position[i] = pos
    height[i] = hei

def left_domino(idx):
    length = position[idx]+height[idx]

    cnt = 1
    for i in range(idx+1, N):
        if height[i]:
            if position[i] <= length:
                cnt += 1
                _length = position[i]+height[i]
                if _length > length: length = _length
            else: return cnt
    return cnt

def right_domino(idx):
    length = position[idx]-height[idx]
    if length < 0: length = 0

    cnt = 1
    for i in range(idx-1, -1, -1):
        if height[i]:
            if position[i] >= length:
                cnt += 1
                _length = position[i]-height[i]
                if _length < length: length = _length
            else: return cnt
    return cnt

answer = []
domino = [0 for _ in range(N)]


def find(_height):
    for i in range(N):
        if _height[i]:
            num1 = left_domino(i)
            num2 = right_domino(i)
            domino[i] = (num1, num2)
        else:
            domino[i] = (0, 0)
    maxV, idx = 0, -1
    for i in range(N):
        l, r = domino[i]
        if maxV < l: maxV, idx = l, i
        if maxV < r: maxV, idx = r, i

    return maxV, idx

from collections import deque
from copy import deepcopy

cnt, idx = find(height)
Queue = deque()
for i in range(2):
    if domino[idx][i]: Queue.append((N, 1, domino[idx][i], idx, i, deepcopy(height)))

while Queue:
    rem, ans, cnt, idx, state, hei = Queue.popleft()
    print(rem, domino)
    
    rev = 0
    for i in range(idx, -1 if state else N, -1 if state else 1):
        if hei[i]:
            hei[i] = 0
            rev += 1
        if rev == cnt:
            break
    
    rem -= cnt
    if rem == 0:
        answer.append(ans)
        continue
    
    cnt, idx = find(hei)
    for i in range(2):
        if domino[idx][i]: Queue.append((rem, ans+1, domino[idx][i], idx, i, deepcopy(hei)))

print(min(answer))