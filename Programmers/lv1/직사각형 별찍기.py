# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12969

def solution(ipt):
    a, b = map(int, ipt.strip().split(' '))
    answer = ""
    for j in range(b):
        for i in range(a):
            answer += '*'
        answer += '\n'
    return answer

ipt = [
    "5 3",
    "2 2"
]

result = [
    "*****\n*****\n*****\n",
    "**\n**\n"
]

for q in [0,1]:
    qid = solution(ipt[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')