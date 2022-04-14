# 정렬
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    for i in range(citations[0], 0, -1):
        count1 = 0
        for j in citations:
            if i <= j:
                count1 += 1
            if count1 >= i:
                return i
    return 0

citations = [
    [3, 0, 6, 1, 5],
    [1241, 555, 1255, 552, 5]
]

result = [
    3,
    5
]

for q in [0,1]:
    qid = solution(citations[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')