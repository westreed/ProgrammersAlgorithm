# 탐욕법(Greedy)
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
	answers = 0
	std = [1] * n
	for k in reserve:
		std[k-1] = 2
	for i in lost:
		std[i-1] = std[i-1] - 1
	for j in range(0,n):
		if std[j] == 0:
			if j == 0:
				if std[j+1] == 2:
					std[j] = 1
					std[j+1] = 1
			elif j == (n-1):
				if std[j-1] == 2:
					std[j] = 1
					std[j-1] = 1
			else:
				if std[j-1] == 2:
					std[j] = 1
					std[j-1] = 1
				else:
					if std[j+1] == 2:
						std[j] = 1
						std[j+1] = 1
	for l in range(0,n):
		if std[l] >= 1:
			answers = answers + 1
	return answers

n = [
    5,
    5,
    3
]

lost = [
    [2,4],
    [2,4],
    [3]
]

reserve = [
    [1,3,5],
    [3],
    [1]
]

result = [
    5,
    4,
    2
]

for q in [0,1,2]:
    qid = solution(n[q], lost[q], reserve[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')