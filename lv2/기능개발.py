# 스택/큐
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    from math import ceil

    answer = []
    complete = []
    for i in range(len(progresses)):
        remain = 100-progresses[i]
        days = ceil(remain / speeds[i])
        complete.append(days)
    
    print(complete)
    sameDist  = 1
    checkDays = complete[0]
    for i in range(1,len(complete)):
        if checkDays < complete[i]:
            checkDays = complete[i]
            answer.append(sameDist)
            sameDist = 1
        else:
            sameDist += 1
    
    if checkDays < complete[-1]: answer.append(sameDist)
    else: answer.append(sameDist)
    
    return answer

    

    # pro_len = len(progresses)
    # a = True
    # order = 0
    # answer = []
    # while (a == True):
    #     temp = 0
    #     for i in range(pro_len):
    #         if (progresses[i] < 100):
    #             progresses[i] += speeds[i]
    #         if (order == i and progresses[i] >= 100):
    #             order += 1
    #             temp += 1
    #     if (temp >= 1):
    #          answer.append(temp)
    #     if (order == pro_len):
    #         a = False
    # return answer

progresses = [
    [93, 30, 55],
    [95, 90, 99, 99, 80, 99]
]

speeds = [
    [1, 30, 5],
    [1, 1, 1, 1, 1, 1]
]

result = [
    [2, 1],
    [1, 3, 2]
]

for q in [0,1]:
    qid = solution(progresses[q], speeds[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')