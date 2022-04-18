# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):

    def moveHanoi(n, From=1, Temp=2, To=3):
        ret = []
        if n == 1:
            print(From, To)
            return [From, To]
        moveHanoi(n-1, From, To, Temp)
        ret.append([From, To])
        moveHanoi(n-1, Temp, From, To)
        return ret
    
    a = moveHanoi(n)
    print(a)

n = [
    2
]
result = [
    [[1,2], [1,3], [2,3]]
]

for q in [0]:
    qid = solution(n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')