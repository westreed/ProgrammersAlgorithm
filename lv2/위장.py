# 해시
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    from functools import reduce

    answer = 0
    clothes_type = {}

    for c in clothes:
        types = c[1] #headgear, eyewear, ...
        if clothes_type.get(types): clothes_type[types] += 1
        else: clothes_type[types] = 2

    clothes_num = list(clothes_type.values())
    
    answer = reduce(lambda x, y: x * y, clothes_num)-1
    return answer

clothes = [
    [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],
    [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
]

result = [
    5,
    3
]

for q in [0,1]:
    qid = solution(clothes[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')