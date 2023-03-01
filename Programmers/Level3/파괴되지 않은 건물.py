# 2022 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    Answer = 0
    N, M = len(board[0]), len(board)
    
    _skill = [[0 for _ in range(N)] for _ in range(M)]
    for type, r1, c1, r2, c2, degree in skill:
        value = -degree if type == 1 else degree
        _skill[r1][c1] += value
        if c2+1 < N: _skill[r1][c2+1] += -value
        if r2+1 < M: _skill[r2+1][c1] += -value
        if c2+1 < N and r2+1 < M: _skill[r2+1][c2+1] += value
    
    for x in range(1, N):
        for y in range(M):
            _skill[y][x] += _skill[y][x-1]
    
    for y in range(1, M):
        for x in range(N):
            _skill[y][x] += _skill[y-1][x]
    
    for y in range(M):
        for x in range(N):
            board[y][x] += _skill[y][x]
            if board[y][x] > 0: Answer += 1
    
    return Answer


board = [
    [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
    [[1,2,3],[4,5,6],[7,8,9]]
]

skill = [
    [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]],
    [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
]

result = [
    10,
    6
]

for q in [0,1]:
    qid = solution(board[q], skill[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')