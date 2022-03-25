# 찾아라 프로그래밍 마에스터
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    half = int(len(nums)/2)
    types = len(list(set(nums)))
    if(types > half):
        return half
    else:
        return types

nums = [
    [3,1,2,3],
    [3,3,3,2,2,4],
    [3,3,3,2,2,2]
]

result = [
    2,
    3,
    2
]

for q in [0,1,2]:
    qid = solution(nums[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')