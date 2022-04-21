# 그래프
# https://programmers.co.kr/learn/courses/30/lessons/49191

def dfs(pos, end, record):
    cnt = 0
    if pos == end:
        return 1
    
    for p in record[pos]:
        cnt += dfs(p, end, record)

    return cnt


def solution(n, results):
    from collections import defaultdict
    rank = [list(range(n)) for _ in range(n)]
    record = defaultdict(list)

    for re in results:
        win, lose = re
        record[win].append(lose)
    
    print(record)
    
    result_l = [[len(record[i+1]),0] for i in range(n)]
    for i in range(n): # 승자
        for j in range(n): # 패자
            if i != j:
                result_l[j][1] += 1 if dfs(i+1, j+1, record) > 0 else 0
    
    print(result_l)

    


n = [
    5
]
results = [
    [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
]
result = [
    2
]

for q in [0]:
    qid = solution(n[q], results[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')