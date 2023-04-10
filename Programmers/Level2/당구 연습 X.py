# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/169198?language=python3

def solution(m, n, startX, startY, balls):
    answer = []
    for ballX, ballY in balls:
        min_results = []

        # Top, Bottom
        for standY in [0, n]:
            start_diff_Y = abs(standY - startY)
            ball_diff_Y = abs(standY - ballY)
            diff_X = abs(startX - ballX)
            ball_diff_X = diff_X / (start_diff_Y / ball_diff_Y + 1)
            start_diff_X = diff_X - ball_diff_X
            if start_diff_X == 0.0 or ball_diff_X == 0.0: break

            start_length = (start_diff_X**2 + start_diff_Y**2)**0.5
            ball_length = (ball_diff_X**2 + ball_diff_Y**2)**0.5
            
            min_results.append(int(round((start_length + ball_length)**2, 0)))
        
        # Left, Right
        for standX in [0, m]:
            start_diff_X = abs(standX - startX)
            ball_diff_X = abs(standX - ballX)
            diff_Y = abs(startY - ballY)
            ball_diff_Y = diff_Y / (start_diff_X / ball_diff_X + 1)
            start_diff_Y = diff_Y - ball_diff_Y
            if start_diff_Y == 0.0 or ball_diff_Y == 0.0: break

            start_length = (start_diff_X**2 + start_diff_Y**2)**0.5
            ball_length = (ball_diff_X**2 + ball_diff_Y**2)**0.5
            min_results.append(int(round((start_length + ball_length)**2, 0)))
        
        print(min_results)
        answer.append(min(min_results))
    return answer


m = [10, 10]
n = [10, 10]
startX = [3, 3]
startY = [7, 3]
balls = [[[7, 7], [2, 7], [7, 3]], [[5,5]]]
result = [[52, 37, 116], [200]]

for q in [1]:
    qid = solution(m[q], n[q], startX[q], startY[q], balls[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')