# 2019 카카오 개발자 겨울 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    re = {}
    s = s.replace("{{","").replace("}}","").split("},{")
    for i in s:
        a = set(i.split(","))
        re[i.count(",")] = a
    
    answer = [int(list(re[0])[0])]
    for i in range(len(re)-1):
        answer.append(int(list(re[i+1]-re[i])[0]))
    
    return answer

s = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}"
]

result = [
    [2, 1, 3, 4],
    [2, 1, 3, 4],
    [111, 20],
    [123],
    [3, 2, 4, 1]
]

for q in [0,1,2,3]:
    qid = solution(s[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')