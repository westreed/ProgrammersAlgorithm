# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
	string = "수박"
	divalue = divmod(n, 2)
	answer = string*(divalue[0])
	if divalue[1] == 1:
		answer += "수"
	return answer

n = [3,4]
result = ["수박수", "수박수박"]

for q in [0,1]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')