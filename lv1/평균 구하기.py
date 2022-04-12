# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12944

def solution (arr):
    return sum(arr)/len(arr)

arr = [
    [1,2,3,4],
    [5,5]
]

result = [
    2.5,
    5
]

for q in [0,1]:
    qid = solution(arr[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')