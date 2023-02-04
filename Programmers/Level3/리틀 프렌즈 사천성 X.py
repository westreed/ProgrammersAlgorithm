# 2017 카카오코드 본선
# https://programmers.co.kr/learn/courses/30/lessons/1836

def solution(m, n, board):
    board = list(map(list, board))
    for b in board:
        print(b)

m = [
    3,
    2,
    4,
    2,
    4
]

n = [
    3,
    4,
    4,
    2,
    4
]

board = [
    ["DBA", "C*A", "CDB"],
    ["NRYN", "ARYA"],
    [".ZI.", "M.**", "MZU.", ".IU."],
    ["AB", "BA"],
    ["A...", "..B.", "B...", "...A"]
]

result = [
    "ABCD",
    "RYAN",
    "MUZI",
    "IMPOSSIBLE",
    "AB"
]

for q in [2]:
    qid = solution(m[q], n[q], board[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')