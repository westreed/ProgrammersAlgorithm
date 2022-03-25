# 정렬
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
	answerlist = []
	for cmd in commands:
		a = array[cmd[0]-1:cmd[1]]
		a.sort()
		answer = a[cmd[2]-1]
		answerlist.append(answer)
	return answerlist

array = [
    [1, 5, 2, 6, 3, 7, 4]
]

commands = [
    [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
]

result = [
    [5,6,3]
]

for q in [0]:
    qid = solution(array[q], commands[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')