# 탐욕법(Greedy)
# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    number = list(number)
    length,nine = len(number),number.count('9')
    
    if (length - nine) <= k:
        return '9'*(length-k)
    
    for i in range(k):
        for n in range(length-i-1):
            if number[n] == '9': continue
            if number[n+1] > number[n]:
                del number[n]
                break
        else: number.pop()
        
    return ''.join(number)

number = [
    "1924",
    "1231234",
    "4177252841"
]

k = [
    2,
    3,
    4
]

result = [
    "94",
    "3234",
    "775841"
]

for q in [0,1,2]:
    qid = solution(number[q], k[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')