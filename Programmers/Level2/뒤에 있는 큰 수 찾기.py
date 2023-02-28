# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/154539
   
def solution(numbers):
    from collections import deque
    bignum = [-1 for _ in range(len(numbers))]
    stack = deque()
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            bignum[stack.pop()] = numbers[i]
        stack.append(i)
    
    return bignum

numbers = [
    [2, 3, 3, 5],
    [9, 1, 5, 3, 6, 2]
]

result = [
    [3, 5, 5, -1],
    [-1, 5, 6, 6, -1, -1]
]

for q in [0, 1]:
    qid = solution(numbers[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')