# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
# https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3

def solution(lottos, win_nums):
    # zero  0의 갯수 (0은 조커임)
    # check 알수 있는 값중 일치하는 수
    zero, check = 0, 0
    lotto = [6, 6, 5, 4, 3, 2, 1]

    for num in lottos:
        if(num == 0):
            zero += 1
        elif num in win_nums:
            win_nums.remove(num)
            check += 1

    return [lotto[check+zero], lotto[check]]

lottos = [
    [44, 1, 0, 0, 31, 25],
    [0, 0, 0, 0, 0, 0],
    [45, 4, 35, 20, 3, 9]
]

win_nums = [
    [31, 10, 45, 1, 6, 19],
    [38, 19, 20, 40, 15, 25],
    [20, 9, 3, 45, 4, 35]
]

result = [
    [3,5],
    [1,6],
    [1,1]
]

for q in [0,1,2]:
    qid = solution(lottos[q], win_nums[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')