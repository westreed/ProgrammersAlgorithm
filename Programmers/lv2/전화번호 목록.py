# 해시
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if(phone_book[i+1].startswith(phone_book[i])):
            return False
    return True

phone_book = [
    ["119", "97674223", "1195524421"],
    ["123","456","789"],
    ["12","123","1235","567","88"]
]

result = [
    False,
    True,
    False
]

for q in [0,1,2]:
    qid = solution(phone_book[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')