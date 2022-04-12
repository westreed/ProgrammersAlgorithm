# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    if s[0] == "-":
        return -int(s[1:], 10)
    else:
        return int(s, 10)

s = [
    "1234",
    "-1234"
]

result = [
    1234,
    -1234
]

for q in [0,1]:
    qid = solution(s[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')