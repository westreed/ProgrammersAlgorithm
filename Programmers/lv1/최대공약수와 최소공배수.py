# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12940

def swap(n, m):
    if n < m:
        t = n
        n = m
        m = t
    return n, m

def max(n, m):
    r = n % m
    return max(m, r) if r else m

def solution (n,m):
    answer = ['GCD','LCM']
    n, m = swap(n, m)
    GCD  = max(n, m)
    answer[0] = GCD
    answer[1] = int((n*m)/GCD)
    return answer

    




n = [
    3,
    2
]

m = [
    12,
    5
]

result = [
    [3,12],
    [1,10]
]

for q in [0,1]:
    qid = solution(n[q], m[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')