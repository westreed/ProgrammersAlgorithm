# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    phone_length = len(phone_number)-4
    return '*'*phone_length + phone_number[-4:]

phone_number = [
    "01033334444",
    "027778888"
]

result = [
    "*******4444",
    "*****8888"
]

for q in [0,1]:
    qid = solution(phone_number[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')