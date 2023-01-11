# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    splits = s.split(" ")
    if splits == []: return s
    answer = []
    for i in range(len(splits)):
        string = ''
        for j in range(len(splits[i])):
            if j%2 == 0:
                string += splits[i][j].upper()
            else:
                string += splits[i][j].lower()
        answer.append(string)
    answer = " ".join(answer)
    return answer

s = ["try hello world"]
result = ["TrY HeLlO WoRlD"]

for q in [0]:
    qid = solution(s[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')