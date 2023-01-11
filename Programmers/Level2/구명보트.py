# 탐욕법(Greedy)
# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    people.sort()
    loopN = len(people)
    index = 0
    while(loopN+1):
        n = people[loopN-1]
        
        for i in range(index,loopN):
            if(loopN < 2 or limit-n < people[i]):
                answer += 1
                break
            else:
                index += 1
                answer += 1
                break
        loopN -= 1
    return answer

people = [
    [70, 50, 80, 50],
    [70, 80, 50]
]

limit = [
    100,
    100
]

result = [
    3,
    3
]

for q in [0,1]:
    qid = solution(people[q], limit[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')