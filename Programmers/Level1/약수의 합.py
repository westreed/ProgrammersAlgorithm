# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    if n == 0: return 0
    if n == 1: return 1

    div = [1,n]
    for i in range(2,n):
        if (n%i) == 0:
            div.append(i)
            
    answer = sum(div)
    return answer

n = [12, 5]
result = [28, 6]

for q in [0,1]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')