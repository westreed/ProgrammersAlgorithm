# 월간 코드 챌린지 시즌3
# https://programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    length = right-left+1
    array = [0 for _ in range(length)]

    row,column = divmod(left, n)

    for idx in range(length):
        if column < row:
            array[idx] = row+1
        else:
            array[idx] = column+1
        
        if column == n-1:
            column = 0
            row += 1
        else: column += 1
    
    return array


n = [
    3,
    4
]

left = [
    2,
    7
]

right = [
    5,
    14
]

result = [
    [3,2,2,3],
    [4,3,3,3,4,4,4,4],
]

for q in [0,1]:
    qid = solution(n[q], left[q], right[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')