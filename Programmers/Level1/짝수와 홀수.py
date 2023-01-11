# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12937

def solution(num):
    return "Odd" if num % 2 else "Even"

num = [
    3,
    4
]

result = [
    "Odd",
    "Even"
]

for q in [0,1]:
    qid = solution(num[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')