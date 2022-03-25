# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
	return s.isdigit() and (len(s) == 4 or len(s) == 6)

s = [
    "a234",
    "1234"
]

result = [
    False,
    True
]

for q in [0,1]:
    qid = solution(s[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')