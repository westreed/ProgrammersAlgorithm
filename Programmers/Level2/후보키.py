# 2019 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/42890

def solution(relation):
    from collections import deque
    from itertools import combinations
    dataNum     = len(relation)
    classNum    = len(relation[0])

    candidateKeys = []
    for i in range(1, classNum+1):
        candidateKeys.extend(list(combinations(range(classNum), i)))
    
    index = 0
    while True:
        if len(candidateKeys) <= index: break

        key = candidateKeys[index]
        data = []
        # 선정된 후보키에 따라 각 튜플의 데이터 가져오기
        for i in range(dataNum):
            lineData = ''
            for c in key:
                lineData += f'{relation[i][c]} '
            data.append(lineData)
        
        # 중복된 데이터가 있는지 체크하기
        nextLoop = False
        for i in range(dataNum):
            if data.count(data[i]) > 1:
                del candidateKeys[index]
                nextLoop = True
                break
        if nextLoop: continue
        
        # 중복된 데이터가 없으면 최소성을 위해 해당 후보키가 포함된
        # 다른 후보키들을 삭제한다
        tempKeys = deque(candidateKeys[index+1:])
        candidateKeys = candidateKeys[:index+1]
        while tempKeys:
            curKey = tempKeys.popleft()
            stack = 0
            for c in key:
                if c in curKey:
                    stack += 1

            if stack != len(key):
                candidateKeys.append(curKey)

        index += 1

    print(candidateKeys)
    return len(candidateKeys)

relation = [
    [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
]

result = [
    2
]

for q in [0]:
    qid = solution(relation[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')