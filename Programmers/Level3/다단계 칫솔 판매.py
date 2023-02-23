# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
# https://school.programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):
    Pays = {name : 0 for name in enroll}
    Maps = {enroll[idx] : refer for idx, refer in enumerate(referral)}
    
    for name, money in zip(seller, amount):
        save = money*100
        while True:
            if name != "-":
                give = save // 10
                save -= give
                Pays[name] += save
                if give == 0: break
                save = give
                name = Maps[name]
            else: break

    return list(Pays.values())

enroll = [
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
]

referral = [
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
]

seller = [
    ["young", "john", "tod", "emily", "mary"],
    ["sam", "emily", "jaimie", "edward"]
]

amount = [
    [12, 4, 2, 5, 10],
    [2, 3, 5, 4]
]

result = [
    [360, 958, 108, 0, 450, 18, 180, 1080],
    [0, 110, 378, 180, 270, 450, 0, 0]
]

for q in [0,1]:
    qid = solution(enroll[q], referral[q], seller[q], amount[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')