# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
	if a == b:
		return a
	else:
		if a < b:
			return (sum(list(range(a,b+1))))
		else:
			return (sum(list(range(a,b-1,-1))))

a = [
    3,
    3,
    5
]

b = [
    5,
    3,
    3
]

result = [
    12,
    3,
    12
]

for q in [0,1,2]:
    qid = solution(a[q], b[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')