# 위클리 챌린지
# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    for s in range(len(sizes)):
        if sizes[s][0] < sizes[s][1]:
            temp = sizes[s][0]
            sizes[s][0] = sizes[s][1]
            sizes[s][1] = temp
    
    max1, max2 = 0,0
    for s in sizes:
        if s[0] > max1: max1 = s[0]
        if s[1] > max2: max2 = s[1]
    
    return max1*max2

sizes = [
    [[60, 50], [30, 70], [60, 30], [80, 40]],
    [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]],
    [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
]

result = [
    4000,
    120,
    133
]

for q in [0,1,2]:
    qid = solution(sizes[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')