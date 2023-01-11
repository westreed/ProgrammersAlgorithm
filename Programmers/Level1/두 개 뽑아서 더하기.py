# 월간 코드 챌린지 시즌1
# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = set() #중복을 제거하기 위해, 집합 생성
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i]+numbers[j])
    answer = list(answer)
    answer.sort()
    return answer

numbers = [
    [2,1,3,4,1],
    [5,0,2,7]
]

result = [
    [2,3,4,5,6,7],
    [2,5,7,9,12]
]

for q in [0,1]:
    qid = solution(numbers[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')