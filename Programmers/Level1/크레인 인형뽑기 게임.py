# 2019 카카오 개발자 겨울 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    choose = [] #뽑은 인형 리스트
    front = -1 #Stack 구조이용하기
    Answer = 0 #반환될 변수
    for m in moves: #크레인 행동
        for l in board: #각 라인 검색
            if(l[m-1] == 0): #해당 라인이 0이면(인형이 없는 경우)
                continue
            else:
                choose.append(l[m-1]) #인형값을 적재리스트에 담음
                front += 1 #스택에 값이 쌓였으므로, +1 시킴.
                if(front > 0 and choose[front] == choose[front-1]):
                #값이 2개이상 쌓인 상태에서 인형값이 이전과 같을때
                    del choose[front]
                    del choose[front-1]
                    front -= 2 #2개의 인형이 스택에서 나가므로, 2를 뺌.
                    Answer += 2
                l[m-1] = 0 #인형을 뽑았으므로, 해당 칸은 0으로 변경함.
                break
    return Answer

board = [
    [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
]
moves = [
    [1,5,3,5,1,2,1,4]
]
result = [
    4
]

for q in [0]:
    qid = solution(board[q], moves[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')