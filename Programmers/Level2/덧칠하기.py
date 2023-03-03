# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    ans = 0
    idx = 0
    for s in section:
        if idx < s:
            idx = s+m-1
            ans += 1
    return ans

n = [8, 5, 4]
m = [4, 4, 1]
section = [
    [2, 3, 6],
    [1, 3],
    [1, 2, 3, 4]
]
result = [2, 1, 4]

for q in [0,1,2]:
    qid = solution(n[q], m[q], section[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')