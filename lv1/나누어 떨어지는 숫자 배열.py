# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
	answer = []
	for i in arr:
		if i%divisor == 0:
			answer.append(i)
	if answer == []:
		return [-1]
	else:
		answer.sort()
		return answer

arr = [
    [5, 9, 7, 10],
    [2, 36, 1, 3],
    [3, 2, 6]
]

divisor = [
    5,
    1,
    10
]

result = [
    [5,10],
    [1,2,3,36],
    [-1]
]

for q in [0,1,2]:
    qid = solution(arr[q], divisor[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')