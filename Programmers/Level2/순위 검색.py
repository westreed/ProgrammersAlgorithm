# 2021 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/72412

def solution(info, query):
    import collections, itertools, bisect

    hashmap = collections.defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))

    for crew in info:
        crew = crew.split()
        for binary in binarys:
            key = ''.join([crew[i] if binary[i] else '-' for i in range(4)]) 
            hashmap[key].append(int(crew[4]))

    for k in hashmap.keys():
        hashmap[k].sort()

    answer = []
    for qu in query:
        lang,_,job,_,career,_,food,score = qu.split()
        key = "".join([lang,job,career,food])
        crew = hashmap[key]
        i = bisect.bisect_left(crew, int(score))
        answer.append(len(crew) - i)
    
    return answer
    


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