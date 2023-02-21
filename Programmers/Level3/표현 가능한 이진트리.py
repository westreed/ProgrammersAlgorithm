# 2023 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/150367

# 아이디어
# 1. 1, 3, 7, 15, 31, 63, ... 와 같은 일정한 길이로 만들 수 있어야 한다.
# 2. 루트는 무조건 1이어야 한다.
# 3. 부모노드가 0이면, 그 밑의 자식노드는 전부 0이어야 한다.

def solution(numbers):
    from collections import deque
    testcase = len(numbers)
    answer = [1] * testcase

    tree = [1, 3, 7, 15, 31, 63]
    treeProb = [-1] * 51
    probIdx, treeIdx = 1, 0
    while probIdx < 51:
        if tree[treeIdx] < probIdx: treeIdx += 1
        treeProb[probIdx] = tree[treeIdx]
        probIdx += 1

    for tc in range(testcase):
        number = numbers[tc]
        _num = bin(number)[2:]
        _len = len(_num)
        # 현재 이진길이에 따라, 만들어야하는 포화이진트리의 갯수
        size = treeProb[_len]
        center = size // 2 + 1
        # 'b'를 붙이는건, center 기준으로 값 계산을 편하게 하기 위해 임의로 추가함
        _num = 'b' + '0'*(size-_len) + _num
        
        # 루트가 0이면, 전부 0이어야 하므로 불가능하다.
        if _num[center] == '0':
            answer[tc] = 0
            continue

        Queue = deque([(center, center//2, False)])
        while Queue:
            root, length, zero = Queue.popleft()
            
            if zero and _num[root] == "1":
                answer[tc] = 0
                break
            elif _num[root] == "0":
                zero = True
            
            # 홀수는 단말노드이므로, 더이상 내려갈 수 없음
            if root % 2 == 1: continue

            _length = length // 2
            Queue.append((root-length, _length, zero))
            Queue.append((root+length, _length, zero))
    return answer


numbers = [
    [7, 42, 5],
    [63, 111, 95]
]

result = [
    [1, 1, 0],
    [1, 1, 0]
]

for q in [0,1]:
    qid = solution(numbers[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')