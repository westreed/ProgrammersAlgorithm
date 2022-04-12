# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    return int("".join(sorted(list(str(int(n))), reverse=True)))

n = [
    118372
]

result = [
    873211
]

for q in [0]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')