# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
	string = len(s)
	center = string//2
	#0이면 글자가 짝수
	if string%2 == 0:
		return s[center-1:center+1]
	else:
		return s[center]
    
s = [
    "abcde",
    "qwer"
]

result = [
    "c",
    "we"
]

for q in [0,1]:
    qid = solution(s[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')