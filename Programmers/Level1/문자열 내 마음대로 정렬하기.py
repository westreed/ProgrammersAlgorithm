# 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    import operator
    answer = []
    strings2 = {}
    for i in strings:
        strings2[i] = i[n]
    print(strings2)
    a = sorted(strings2.items(), key=operator.itemgetter(1, 0))
    print(a)
    for s in a:
        answer.append(s[0])
    return answer

strings = [
    ["sun", "bed", "car"],
    ["abce", "abcd", "cdx"]
]

n = [
    1,
    2
]

result = [
    ["car", "bed", "sun"],
    ["abcd", "abce", "cdx"]
]

for q in [0,1]:
    qid = solution(strings[q], n[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')