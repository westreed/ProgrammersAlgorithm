# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
	weeks = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
	months,days = 1,1
	while months < a:
		if months==1 or months==3 or months==5 or months==7 or months==8 or months==10 or months==12:
			days += 31
		if months==4 or months==6 or months==9 or months==11:
			days += 30
		if months==2:
			days += 29
		months += 1
	days += b-1
	return weeks[days%7]

a = [5]
b = [24]
result = ["TUE"]

for q in [0]:
    qid = solution(a[q], b[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')