# 2018 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/17679

def findSquare(m, n, board):
    x,y = 0,0
    checkBox = []
    while True:
        if board[y][x] == board[y][x+1]:
            tile = board[y][x]
            if board[y+1][x] == tile and board[y+1][x+1] == tile:
                checkBox.append((x,y))
        if y == m-2 and x == n-2: break
        if x < n-2: x += 1
        else: x,y = 0, y+1
    
    dx = [0,1,0,1]
    dy = [0,0,1,1]
    removeTile = 0
    while checkBox:
        tile = checkBox.pop()
        tx,ty = tile[0],tile[1]
        for i in range(4):
            tty,ttx = ty+dy[i],tx+dx[i]
            if board[tty][ttx] != ' ':
                removeTile += 1
                board[tty][ttx] = ' '

    # 만약 반환되는 값이 0이면 종료
    return removeTile

def descendTile(m, n, board):
    for col in range(n):# 각 라인
        checkPoint = []
        for t in range(m-1, -1, -1):
            if board[t][col] == ' ':
                checkPoint.insert(0, t)
            elif checkPoint:
                pos = checkPoint.pop()
                board[pos][col] = board[t][col]
                board[t][col] = ' '
                checkPoint.insert(0, t)

def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = ' '.join(board[i]).split(' ')
    
    while True:
        removeTile = findSquare(m, n, board)
        answer += removeTile
        if removeTile: descendTile(m, n, board)
        else: break
    
    return answer

m = [
    4,
    6
]

n = [
    5,
    6
]

board = [
    ["CCBDE", "AAADE", "AAABF", "CCBBF"],
    ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
]

result = [
    14,
    15
]

for q in [0,1]:
    qid = solution(m[q], n[q], board[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')