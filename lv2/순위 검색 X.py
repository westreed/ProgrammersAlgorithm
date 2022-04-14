# 2021 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/72412

def solution(info, query):
    import heapq
    answer = []
    newCrew = []
    newQuery = []
    for i in info:
        temp = i.split(' ')
        temp.insert(0, int(temp.pop()))
        newCrew.append(temp)
    newCrew.sort(reverse=True)
    
    index = 0
    for q in query:
        temp = q.replace('and ','').split(' ')
        temp.insert(0, int(temp.pop()))
        temp.append(index)
        heapq.heappush(newQuery, temp)
        index += 1
    
    for q in range(len(newQuery)): #n번째 조건
        query = heapq.heappop(newQuery)
        checkCrew = 0
        t = len(newCrew)
        for crew in newCrew:
            if int(query[0]) > int(crew[0]):
                for v in range(t): newCrew.pop()
                break
            t -= 1
        for crew in newCrew: #지원한 사람
            check = True
            for qu in range(1,5):
                if(query[qu] == '-'): continue
                elif(query[qu] != crew[qu]):
                    check = False
                    break
            if check: checkCrew += 1
        answer.append((query[5],checkCrew))
    answer.sort()
    return [i[1] for i in answer]

info = [
    ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
]

query = [
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
]

result = [
    [1,1,1,1,2,4]
]

for q in [0]:
    qid = solution(info[q], query[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')