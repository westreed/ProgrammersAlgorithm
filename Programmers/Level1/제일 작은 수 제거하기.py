# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    length = len(arr)
    if length == 1: return [-1]

    minv = 0
    for i in range(1,length):
        if arr[i] < arr[minv]:
            minv = i
    
    del arr[minv]
    return arr

arr = [
    [4,3,2,1],
    [10]
]

result = [
    [4,3,2],
    [-1]
]

for q in [0,1]:
    qid = solution(arr[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')