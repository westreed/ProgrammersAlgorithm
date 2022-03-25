# 월간 코드 챌린지 시즌3
# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    return sum([i for i in range(1,10) if i not in numbers])

numbers = [
    [1,2,3,4,6,7,8,0],
    [5,8,4,0,6,7,9]
]

result = [
    14,
    6
]

for q in [0,1]:
    qid = solution(numbers[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')