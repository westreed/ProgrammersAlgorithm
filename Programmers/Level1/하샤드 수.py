# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    sum_x = sum(list(map(int,str(x))))
    return True if x % sum_x == 0 else False

x = [
    10,
    12,
    11,
    13
]

result = [
    True,
    True,
    False,
    False
]

for q in [0,1,2,3]:
    qid = solution(x[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')