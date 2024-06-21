# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/138475

def find(counts, desc, start):
    for d in desc:
        nums = counts[d]
        for i in nums:
            if i >= start:
                return i

def solution(e, starts):
    from collections import defaultdict
    divisor = [0 for _ in range(e+1)]
    counts = defaultdict(list)
    divisor[1] = 1

    # 파이썬으로 통과하고 싶으면, 아래의 최적화 기법으로 계산해야됨.
    # for i in range(1, int(e**0.5)+1):
    #     divisor[i**2] += 1

    # 이부분은 이해가 안됨...
    # for i in range(2,e+1):
    #     for j in range(1,min(e//i+1,i)):
    #         divisor[i*j] += 2

    for i in range(2, e+1):
        for j in range(1, e//i+1):
            divisor[i*j] += 1
    
    for i in range(1, e+1):
        counts[divisor[i]].append(i)
    
    desc = sorted(counts.keys(), reverse=True)
    answer = []
    for start in starts:
        res = find(counts, desc, start)
        answer.append(res)

    return answer

e = [8]
starts = [[1,3,7]]
result = [[6,6,8]]

for q in [0]:
    qid = solution(e[q], starts[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')