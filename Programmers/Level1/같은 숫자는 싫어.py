# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
	answer = []
	for i in range(len(arr)):
		if arr[i:i+1] != arr[i+1:i+2]:
			answer.append(arr[i])
	return answer

arr = [
    [1,1,3,3,0,1,1],
    [4,4,4,3,3]
]

result = [
    [1,3,0,1],
    [4,3]
]

for q in [0,1]:
    qid = solution(arr[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')