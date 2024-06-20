# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/161988


def solution(sequence):
    n = len(sequence)
    arr1, arr2 = [], []
    for idx, num in enumerate(sequence):
        if idx % 2 == 0:
            arr1.append(num)
            arr2.append(-num)
        else:
            arr1.append(-num)
            arr2.append(num)
    
    dp1, dp2 = [arr1[0]], [arr2[0]]
    for idx in range(1, n):
        dp1.append(max(dp1[idx-1] + arr1[idx], arr1[idx]))
        dp2.append(max(dp2[idx-1] + arr2[idx], arr2[idx]))
    
    return max(max(dp1), max(dp2))

sequence = [[2, 3, -6, 1, 3, -1, 2, 4]]
result = [10]

for q in [0]:
    qid = solution(sequence[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')