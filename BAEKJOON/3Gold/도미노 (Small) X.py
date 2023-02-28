# 
# https://www.acmicpc.net/problem/14586

input = __import__('sys').stdin.readline
N = int(input())
position, height = [0 for _ in range(N)], [0 for _ in range(N)]
lastPos = position[-1]

for i in range(N):
    pos, hei = map(int, input().split())
    position[i] = pos
    height[i] = hei

def left_domino(idx):
    length = position[idx]+height[idx]

    for i in range(idx+1, N):
        if position[i] <= length:
            _length = position[i] + height[i]
            if _length > length: length = _length
        else: return i-idx
    return 0

def right_domino(idx):
    length = position[idx]-height[idx]

    for i in range(idx-1, -1, -1):
        if height[i]:
            if position[i] >= length:
                _length = position[i] - height[i]
                if _length < length: length = _length
            else: return idx-i
    return 0

domino = [0 for _ in range(N)]
for i in range(N):
    num1 = left_domino(i)
    num2 = right_domino(i)
    domino[i] = (num1, num2)

def find():
    for i in range(N):
        if domino[i] != (0,0):
            num1 = left_domino(i)
            num2 = right_domino(i)
            domino[i] = (num1, num2)
    maxV = 0
    idx, state = -1, -1
    for i in range(N):
        l, r = domino[i]
        if maxV < l: maxV, idx, state = l, i, 0
        if maxV < r: maxV, idx, state = r, i, 1

    return idx, state

answer = 0
remain = N
while remain:
    idx, state = find()
    remain -= domino[idx][state]
    if state == 0: state = idx+domino[idx][state]
    else: state = idx-domino[idx][state]

    for i in range(idx, state, 1 if idx < state else -1):
        domino[i] = (0,0)
        height[i] = 0
    
    answer += 1

print(answer)