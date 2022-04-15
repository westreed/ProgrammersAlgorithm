# 스택/큐
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    length = len(prices)
    answer = []
    for i in range(length):
        sec = 0
        for j in range(i+1, length):
            sec += 1
            if(prices[j] < prices[i]): break
        answer.append(sec)
    return answer

prices = [[1, 2, 3, 2, 3]]
result = [[4, 3, 1, 1, 0]]

for q in [0]:
    qid = solution(prices[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')