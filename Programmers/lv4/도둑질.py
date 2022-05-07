# 동적계획법 (Dynamic Programming)
# https://programmers.co.kr/learn/courses/30/lessons/42897

def dp(money):
    length = len(money)
    caches = [0 for _ in range(length)]
    caches[0] = money[0]
    idx = 1
    while idx < length:
        caches[idx] = max(caches[idx-1], money[idx]+caches[idx-2])
        idx += 1
    return caches[-1]

def solution(money):
    a = dp(money[1:])
    b = dp(money[:-1])
    return max(a,b)


money = [
    [1,2,3,1],
    [1,0,0,4,4,2,1,4],
    [0,0,4,4,2,1,4],
    [999,1000,999,999,0],
    [0,0,0,0,100,0,0,100,0,0,1,1],
    [1000,1,0,1,2,1000,0],
    [90,0,0,95,1,1]
]
result = [
    4,
    10,
    10,
    1999,
    201,
    2001,
    185
]

for q in [0,1,2,3,4,5,6]:
    qid = solution(money[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')