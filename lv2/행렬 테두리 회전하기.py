# 2021 Dev-Matching 웹 백엔드 개발자(상반기)
# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    matrix = [[i+1+(j*columns) for i in range(columns)] for j in range(rows)]
    answer = []
    
    for _,query in enumerate(queries):
        y1,x1,y2,x2 = query[0]-1,query[1]-1,query[2]-1,query[3]-1
        xgrid,ygrid = x2-x1,y2-y1
        
        minX = matrix[y1][x1]
        for y in range(ygrid): #Down
            temp = matrix[y1+y+1][x1]
            if temp < minX: minX = temp
            matrix[y1+y+1][x1] = matrix[y1+y][x1]
            matrix[y1+y][x1] = temp
        
        for x in range(xgrid): #Right
            temp = matrix[y2][x1+x+1]
            if temp < minX: minX = temp
            matrix[y2][x1+x+1] = matrix[y2][x1+x]
            matrix[y2][x1+x] = temp
        
        for y in range(ygrid): #Up
            temp = matrix[y2-y-1][x2]
            if temp < minX: minX = temp
            matrix[y2-y-1][x2] = matrix[y2-y][x2]
            matrix[y2-y][x2] = temp
        
        for x in range(xgrid-1): #Left
            temp = matrix[y1][x2-x-1]
            if temp < minX: minX = temp
            matrix[y1][x2-x-1] = matrix[y1][x2-x]
            matrix[y1][x2-x] = temp
        answer.append(minX)
    
    return answer

rows = [
    6,
    3,
    100
]

columns = [
    6,
    3,
    97
]

queries = [
    [[2,2,5,4],[3,3,6,6],[5,1,6,3]],
    [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]],
    [[1,1,100,97]]
]

result = [
    [8, 10, 25],
    [1, 1, 5, 3],
    [1]
]

for q in [0,1,2]:
    qid = solution(rows[q], columns[q], queries[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')