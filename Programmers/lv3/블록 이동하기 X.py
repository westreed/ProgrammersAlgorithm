# 2020 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/60063

def bfs(start, board):
    from collections import deque

    queue = deque()
    queue.append([start,0])

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while queue:
        node, direction = queue.popleft()
        

def solution(board):
    pass

board = [
    [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
]
result = [
    7
]

for q in [0]:
    qid = solution(board[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')