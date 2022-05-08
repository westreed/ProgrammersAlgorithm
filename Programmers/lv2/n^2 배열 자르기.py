def solution(n, left, right):
    # array = [[0 for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     array[i][i] = i+1
    #     idx = 0
    #     while idx < i:
    #         array[idx][i] = i+1
    #         array[i][idx] = i+1
    #         idx += 1
    
    # array2 = []
    # for a in array:
    #     array2.extend(a)
    # print(array2)
    
    array = []
    
    return array2[left:right+1]

n = [
    3,
    4
]

left = [
    2,
    7
]

right = [
    5,
    14
]

result = [
    [3,2,2,3],
    [4,3,3,3,4,4,4,4]
]

for q in [0,1]:
    qid = solution(n[q], left[q], right[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')