# 정렬
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str, numbers))
    tempnum = []
    for n in numbers:
        i = 0
        temp = n
        length = len(n)
        for _ in range(4-length):
            temp += n[i]
            i += 1
            if length <= i: i = 0
        tempnum.append((temp, n))
    
    tempnum = sorted(tempnum, reverse=True)
    
    answer = ''
    for n in tempnum:
        answer += n[1]
    
    if answer.count('0') == len(answer): return '0'
    return answer

numbers = [
    [6, 10, 2],
    [3, 30, 34, 5, 9]
]

result = [
    "6210",
    "9534330"
]

for q in [0,1]:
    qid = solution(numbers[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')