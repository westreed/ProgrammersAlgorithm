# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
	a = sorted(list(s))
	a.reverse()
	answer = ''
	str(answer)
	for i in range(len(a)):
		answer += a[i]
	return(answer)

s = ["Zbcdefg"]
result = ["gfedcbZ"]

for q in [0]:
    qid = solution(s[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')