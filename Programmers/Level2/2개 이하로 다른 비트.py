# 월간 코드 챌린지 시즌2
# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    
    def search(n):
        if n == 0: return 1
        num, index = n, -1
        while num > 0:
            num,q = divmod(num,2)
            if q == 1: index += 1
            elif index >= 1: return n+(2**index)
            else: return n+1
        return n+(2**index)

    return list(map(search, numbers))

numbers = [
    [2,7]
]

result = [
    [3, 11]
]

for q in [0]:
    qid = solution(numbers[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')