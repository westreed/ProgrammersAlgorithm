# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    primeList = [v for v in range(n+1)]
    primeList[1] = 0

    
    for v in range(2,n+1):
        t = 1
        while True:
            t += 1
            index = v*t
            if index > n: break
            if(primeList[index] > 0 and primeList[index] % v == 0):
                primeList[index] = 0
    
    print(primeList)
    return n-primeList.count(0)+1

	# primenumber = [0, 0]
	# excepted = []
	# num = 2
	# indexvalue = 2
	# for i in range(2,n+1):
	# 	primenumber.append(i)
	# while num <= int(n**0.5):
	# 	excepted.append(num)
	# 	for i in range(num, n+1, num):
	# 		primenumber[i] = 0
	# 	temp = primenumber[:]
	# 	del temp[:indexvalue+1]
	# 	while temp[0] == 0:
	# 		del temp[0]
	# 		indexvalue += 1
	# 	num = temp[0]
	# a = primenumber.count(0)
	# num2 = 0
	# while num2 < a:
	# 	num2 += 1
	# 	primenumber.remove(0)
	# excepted.extend(primenumber)
	# print(excepted)
	# return len(excepted)

n = [
    10,
    5
]

result = [
    4,
    3
]

for q in [0,1]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')