# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
	pNum = s.count('p') + s.count('P')
	yNum = s.count('y') + s.count('Y')
	if pNum == yNum:
		return True
	else:
		return False

s = [
    "pPoooyY",
    "Pyy"
]

result = [
    True,
    False
]

for q in [0,1]:
    qid = solution(s[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')