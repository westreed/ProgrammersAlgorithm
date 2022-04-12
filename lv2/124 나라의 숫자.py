# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    input = n
    answer = []
    while(input):
        input,q = divmod(input, 3)
        if q==0:
            input -= 1
            answer.append(str(4))
        else:
            answer.append(str(q))
    answer.reverse()
    answer = ''.join(answer)
    return answer

n = [
    1,
    2,
    3,
    4,
    15,
    18
]

result = [
    "1",
    "2",
    "4",
    "11",
    "114",
    "124"
]

for q in [0,1,2,3,4,5]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')