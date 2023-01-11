# Summer/Winter Coding(~2018)
# https://programmers.co.kr/learn/courses/30/lessons/12977

def solution(nums):
    import math
    
    length = len(nums)
    producted = []
    for i in range(0,length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                producted.append(nums[i]+nums[j]+nums[k])
    
    answer = 0
    for value in producted: #구한 값들이 소수인지 판별하는 부분
        for i in range(2, int(math.sqrt(value))+1):
            if (value % i == 0): break
        else:
            answer += 1
    return answer

nums = [
    [1,2,3,4],
    [1,2,7,6,4]
]

result = [
    1,
    4
]

for q in [0,1]:
    qid = solution(nums[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')