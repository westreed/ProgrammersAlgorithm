# 2020 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    answer = ''
    return answer

p = [
    "(()())()",
    ")(",
    "()))((()"
]

result = [
    "(()())()",
    "()",
    "()(())()"
]

for q in [0,1,2]:
    qid = solution(p[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')