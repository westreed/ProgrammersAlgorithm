# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/169198?language=python3

def solution(m, n, startX, startY, balls):
    answer = []
    # 시작점을 상하좌우로 대칭해보면, 당구공이 움직이는 경로가 직선이 된다.
    # 제 1사분면을 기준으로 대칭이기 때문에 상, 우는 각 테이블축을 2배로 한 크기에서 좌표를 빼면 나온다.
    symPoint = ((-startX, startY), (startX, -startY), (2*m - startX, startY), (startX, 2*n - startY))

    for ballX, ballY in balls:
        dist = int(1e9)
        for sX, sY in symPoint:
            symball_dist = (sX - ballX)**2 + (sY - ballY)**2
            check_dist = (startX - sX)**2 + (startY - sY)**2

            # 벽에 부딪히기 전에 공에 부딪히는 경우는 제외하기
            # 움직인 거리는 대칭점 사이의 거리보다 커야함
            if not(ballX == sX == startX or ballY == sY == startY) or symball_dist > check_dist:
                dist = min(dist, symball_dist)
            
        answer.append(dist)
    return answer


m = [10, 10]
n = [10, 10]
startX = [3, 3]
startY = [7, 3]
balls = [[[7, 7], [2, 7], [7, 3]], [[5,5]]]
result = [[52, 37, 116], [68]]

for q in [0,1]:
    qid = solution(m[q], n[q], startX[q], startY[q], balls[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')