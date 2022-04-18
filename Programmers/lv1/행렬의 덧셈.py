# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
	answer = arr1
	for j in range(len(arr1)):
		for i in range(len(arr1[0])):
			answer[j][i] = arr1[j][i] + arr2[j][i]
	return answer

arr1 = [
    [[1,2],[2,3]],
    [[1],[2]]
]

arr2 = [
    [[3,4],[5,6]],
    [[3],[4]]
]

result = [
    [[4,6],[7,9]],
    [[4],[6]]
]

for q in [0,1]:
    qid = solution(arr1[q], arr2[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')