# 위클리 챌린지
# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    total = int((2*price + (count-1)*price)*count/2)
    if(total <= money):
        return 0
    else:
        return total-money

price = [3]
money = [20]
count = [4]
result = [10]

for q in [0]:
    qid = solution(price[q], money[q], count[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')