# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12926

# a ~ z 97 ~ 122
# A ~ Z 65 ~ 90

def solution(s, n):
    string = ''
    for i in s:
        # 공백인 경우
        if i == ' ':
            string += ' '
            continue

        a = ord(i)
        b = a + n

        if a <= 90 and b > 90: b -= 26
        if a <= 122 and b > 122: b -= 26

        string += chr(b)
    return string

s = [
    "AB",
    "z",
    "a B z"
]

n = [
    1,
    1,
    4
]

result = [
    "BC",
    "a",
    "e F d"
]

for q in [0,1,2]:
    qid = solution(s[q], n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')