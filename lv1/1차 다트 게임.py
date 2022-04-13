# 2018 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    #S 1제곱
    #D 2제곱
    #T 3제곱
    #* 2배 (다른 *과 중첩 가능)
    answer = 0
    dartBonus = {'S':1, 'D':2, 'T':3}
    rewardBonus = ['*', '#']
    index = 3
    starBonus = 1
    dartResult = dartResult.replace("10", "K")
    for s in range(len(dartResult)-1, -1, -1):
        if dartResult[s] in dartBonus:
            index -= 1
            score = 0
            bonusValue = 1
            dartType = dartResult[s]
            if dartResult[s-1] == 'K': score = 10
            else: score = int(dartResult[s-1])
                
            if s < len(dartResult)-1 and dartResult[s+1] in rewardBonus:
                option = dartResult[s+1]
                if option == '*': bonusValue,starBonus = 2*starBonus,2
                else: bonusValue,starBonus = -starBonus, 1
                if score != 0: answer += (score**dartBonus[dartType])*bonusValue
            else:
                bonusValue = starBonus
                if score != 0: answer += (score**dartBonus[dartType])*bonusValue
                starBonus = 1
    return answer

dartResult = [
    "1S2D*3T",
    "1D2S#10S",
    "1D2S0T",
    "1S*2T*3S",
    "1D#2S*3S",
    "1T2D3D#",
    "1D2S3T*"
]

result = [
    37,
    9,
    3,
    23,
    5,
    -4,
    59
]

for q in range(len(result)):
    qid = solution(dartResult[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')