# 완전탐색
# https://programmers.co.kr/learn/courses/30/lessons/42839

def solution(numbers):
    answer = 0
    prime = []
    def search(string, length, depth, number):
        if depth > 0: prime.append(int(number))
        for s in string:
            if depth == 0 and s == '0': continue
            temp = string[:]
            temp.remove(s)
            search(temp, length, depth+1, number+s)
    search(list(numbers), len(numbers), 0, '')
    prime = set(prime)
    for p in prime:
        c = 2
        while c < p:
            if p % c == 0: c = p+1
            else: c += 1
        if c != p+1: answer += 1
    return answer

numbers = [
    "17",
    "011"
]

result = [
    3,
    2
]

for q in [0,1]:
    qid = solution(numbers[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')