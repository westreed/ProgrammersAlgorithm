# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/160585

def checkLine(board):
    Line = {"O":0, "X":0, ".":0}
    if board[0][0] == board[0][1] == board[0][2]: Line[board[0][0]] += 1
    if board[1][0] == board[1][1] == board[1][2]: Line[board[1][0]] += 1
    if board[2][0] == board[2][1] == board[2][2]: Line[board[2][0]] += 1
    if board[0][0] == board[1][0] == board[2][0]: Line[board[0][0]] += 1
    if board[0][1] == board[1][1] == board[2][1]: Line[board[0][1]] += 1
    if board[0][2] == board[1][2] == board[2][2]: Line[board[0][2]] += 1
    if board[0][0] == board[1][1] == board[2][2]: Line[board[0][0]] += 1
    if board[2][0] == board[1][1] == board[0][2]: Line[board[2][0]] += 1
    return Line

def solution(board):
    from collections import defaultdict
    Count = defaultdict(int)
    for y in range(3):
        for x in range(3):
            Count[board[y][x]] += 1
    
    if Count["O"] < Count["X"]: return 0
    if abs(Count["O"]-Count["X"]) >= 2: return 0
    
    Line = checkLine(board)
                
    # if Line["O"] + Line["X"] > 1: return 0 해당 경우에도 0이 되어야 하는데 문제에 오류가 있음
    if Line["O"] and Count["O"] == Count["X"]: return 0
    if Line["X"] and Count["O"] > Count["X"]: return 0
    return 1

board = [
    ["O.X", ".O.", "..X"],
    ["OOO", "...", "XXX"],
    ["...", ".X.", "..."],
    ["...", "...", "..."]
]

result = [
    1, 0, 0, 1
]

for q in [0,1,2,3]:
    qid = solution(board[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')