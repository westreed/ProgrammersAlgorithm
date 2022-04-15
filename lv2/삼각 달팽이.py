# 월간 코드 챌린지 시즌1
# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    Array = [[0 for i in range(j+1)] for j in range(n)]
    Number = 1
    MaxN = sum(range(1,n+1))
    x,y = 0,0
    x1,x2,y1,y2 = 0,n,0,n
    
    while Number < MaxN:
        #밑으로
        while y < y2-1:
            Array[y][x] = Number
            Number += 1
            y += 1
        x1 += 1
        y1 += 1

        #오른쪽으로
        while x < x2-1:
            Array[y][x] = Number
            Number += 1
            x += 1
        y2 -= 1
        x2 -= 1

        #대각선으로
        while x > x1 and y > y1:
            Array[y][x] = Number
            Number += 1
            x -= 1 
            y -= 1

        x2 -= 1
    Array[y][x] = Number

    for i in Array: answer += i

    return answer

n = [
    4,
    5,
    6
]

result = [
    [1,2,9,3,10,8,4,5,6,7],
    [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9],
    [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
]

for q in [0,1,2]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')