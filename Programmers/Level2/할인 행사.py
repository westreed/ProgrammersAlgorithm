# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    from collections import defaultdict
    nums = {want[i] : number[i] for i in range(len(want))}
    want = set(want)
    last = len(discount)
    ans, idx = 0, 0
    while idx+10 <= last:
        inventory = defaultdict(int)
        for i in range(idx, idx+10):
            item = discount[i]
            if item not in want: break
            inventory[item] += 1
            if inventory[item] > nums[item]: break
        else: ans += 1
        idx += 1
    return ans

want = [
    ["banana", "apple", "rice", "pork", "pot"],
    ["apple"]
]

number = [
    [3, 2, 2, 2, 1],
    [10]
]

discount = [
    ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"],
    ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
]

result = [3, 0]

for q in [0,1]:
    qid = solution(want[q], number[q], discount[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')