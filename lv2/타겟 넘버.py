# 깊이/너비 우선 탐색(DFS/BFS)
# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    
    def dfs(index, value, numbers, target):
        ret = 0
        if(index == len(numbers)):
            if(target == value):
                return 1
            return 0
        ret += dfs(index+1, value+numbers[index], numbers, target)
        ret += dfs(index+1, value-numbers[index], numbers, target)
        return ret

    return dfs(0, 0, numbers, target)

numbers = [
    [1, 1, 1, 1, 1],
    [4, 1, 2, 1]
]

target = [
    3,
    4
]

result = [
    5,
    2
]

for q in [0,1]:
    qid = solution(numbers[q], target[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')