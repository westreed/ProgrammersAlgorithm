# 2021  KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/72411

def solution(orders, course):
    from itertools import combinations

    answer = []
    charText = {chr(id+65) : 0 for id in range(26)}
    length = {order:len(order) for order in orders}
    letter = []

    for order in orders:
        for char in order:
            charText[char] += 1
            if charText[char] == 2:
                letter.append(char)
    letter.sort()

    for c in course:
        atLeast = 2
        courseAnswer = []

        # 생성된 조합리스트를 순회
        for cl in combinations(letter, c):
            num = 0
            for order in orders:
                if length[order] < c: continue
                for o in cl:
                    if o not in order: break
                else: num += 1


            if(num >= atLeast):
                createLetter = "".join(cl)
                if(num > atLeast):
                    atLeast = num
                    courseAnswer = [createLetter]
                else:
                    courseAnswer.append(createLetter)
        answer.extend(courseAnswer)

    return sorted(answer)

orders = [
    ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
    ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
    ["XYZ", "XWY", "WXA"]
]

course = [
    [2,3,4],
    [2,3,5],
    [2,3,4]
]

result = [
    ["AC", "ACDE", "BCFG", "CDE"],
    ["ACD", "AD", "ADE", "CD", "XYZ"],
    ["WX", "XY"]
]

for q in [0,1,2]:
    qid = solution(orders[q], course[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')