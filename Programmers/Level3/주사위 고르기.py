# 2024 KAKAO WINTER INTERNSHIP
# https://school.programmers.co.kr/learn/courses/30/lessons/258709

"""
！생각포인트
- 먼저, 선택할 수 있는 주사위 조합을 먼저 계산함. (combinations 활용)
- 조합은 (선택된 조합) vs (나머지 조합) 형태로 만듬.
- 각 주사위 조합에서 나올 수 있는 주사위 합을 계산함.
    - 이 부분도 실제 카카오 코테를 풀 때, for문과 if문을 조합한 괴랄한 형태로 만들었었음...
    - 이러한 경우에는 재귀를 이용한 완전탐색으로 구현하기
- 각 대결구도에 따라 승리횟수를 계산함.
    - 이때, 이분탐색을 활용해서 승리횟수를 카운팅할 생각을 못했음... (최적화 포인트)
    - 이분탐색을 활용하니 계산시간이 개선되어 통과!
"""

def comb_dice(_dice, dice_idx, sums, dice_comb_list):
    if dice_idx == len(_dice):
        dice_comb_list.append(sums)
        return

    for num in _dice[dice_idx]:
        comb_dice(_dice, dice_idx+1, sums+num, dice_comb_list)

def calculate_dice(dice_group, dice):
    dice_comb_list = []
    comb_dice([dice[idx] for idx in dice_group], 0, 0, dice_comb_list)
    dice_comb_list.sort()
    return dice_comb_list

def compare_dice(group1, group2):
    # Group1을 기준
    win = 0
    for target_num in group1:
        left = 0
        right = len(group2)

        while left+1 < right:
            mid = (left+right) // 2
            if target_num > group2[mid]:
                left = mid
            else:
                right = mid
        
        if target_num > group2[left]:
            win += left+1

    return win


def solution(dice):
    from itertools import combinations

    dice_num = len(dice)
    dice.insert(0, None) # 계산 편의성을 위해 idx를 1부터 시작하게 만듬.
    dice_group = list(combinations(range(1,dice_num+1), dice_num//2))
    comb_cnt = len(dice_group)
    dice_group = [(dice_group[idx], dice_group[comb_cnt-idx-1]) for idx in range(0,comb_cnt//2)]

    win_rate = {}
    for group1, group2 in dice_group:
        dice1 = calculate_dice(group1, dice)
        dice2 = calculate_dice(group2, dice)
        win_rate[group1] = compare_dice(dice1, dice2)
        win_rate[group2] = compare_dice(dice2, dice1)
    
    winner = sorted(win_rate.items(), key=lambda x: x[1])
    return list(winner[-1][0])



dice = [
    [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]],
    [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]],
    [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
]

result = [
    [1,4],
    [2],
    [1,3]
]

for q in [0,1,2]:
    qid = solution(dice[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')