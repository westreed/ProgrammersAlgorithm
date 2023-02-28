# 2023 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def timeByDate(date):
    year, month, days = list(map(int, date.split(".")))
    year -= 2000
    month -= 1
    return year*336 + month*28 + days

def solution(today, terms, privacies):
    from collections import defaultdict
    # 2000 <= YYYY <= 2022 이므로, 날짜데이터를 계산하기 쉬운 int형 자료로 변환하기
    answer = []
    today = timeByDate(today)
    privacy = defaultdict(list)
    
    for idx, data in enumerate(privacies):
        date, types = data.split()
        privacy[types].append((idx, timeByDate(date)))
    
    for data in terms:
        types, term = data.split()
        term = int(term)*28
        
        for idx, date in privacy[types]:
            if term + date <= today:
                answer.append(idx+1)
    
    answer.sort()
    return answer

today = [
    "2022.05.19",
    "2020.01.01"
]

terms = [
    ["A 6", "B 12", "C 3"],
    ["Z 3", "D 5"]
]

privacies = [
    ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
    ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
]

result = [
    [1, 3],
    [1, 4, 5]
]

for q in [0,1]:
    qid = solution(today[q], terms[q], privacies[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')