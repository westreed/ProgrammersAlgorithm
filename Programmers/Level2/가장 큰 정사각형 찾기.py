# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    M,N = len(board[0]),len(board)

    if M < 2 or N < 2:
        for b in board:
            if 1 in b: return 1
        return 0
    
    answer = 0
    for y in range(1,N):
        for x in range(1,M):
            if board[y][x] == 1:
                _temp = min(board[y][x-1]+1, board[y-1][x]+1, board[y-1][x-1]+1)
                if answer < _temp: answer = _temp
                board[y][x] = _temp
    
    return answer*answer

board = [
    [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]],
    [[0,0,1,1],[1,1,1,1]]
]

result = [
    9,
    4
]

for q in [0,1]:
    qid = solution(board[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')