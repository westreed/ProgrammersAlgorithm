# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
	return ("김서방은 %d에 있다" %seoul.index('Kim'))

seoul = [["Jane", "Kim"]]
result = ["김서방은 1에 있다"]

for q in [0]:
    qid = solution(seoul[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')