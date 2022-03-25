# 월간 코드 챌린지 시즌2
# https://programmers.co.kr/learn/courses/30/lessons/77884

def divisor(value):
    re = 0
    n = 1
    while n <= value:
        a,b = divmod(value, n)
        if b == 0: re += 1
        n += 1
    if re % 2 == 0: return value
    else: return -value
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        answer += divisor(num)
    return answer

left = [
    13,
    24
]

right = [
    17,
    27
]

result = [
    43,
    52
]

for q in [0,1]:
    qid = 0
    for i in range(left[q], right[q]+1):
        qid += divisor(i)
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')