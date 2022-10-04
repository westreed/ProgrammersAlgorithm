# 연습문제
# https://school.programmers.co.kr/learn/courses/30/lessons/12936

lastN = 0
def solution(n, k):
    
    lasts = []
    bit = [2**i for i in range(n)]
    bit = tuple(bit)
    def dfs(n,k,visit,path=[],length=0):
        global lastN
        if length == n:
            lastN += 1
            lasts.append(path)
            return True
        if lastN == k: return True
        for i in range(n):
            if not visit & bit[i]:
                dfs(n,k,visit+bit[i],path+[i+1],length+1)
    
    dfs(n,k,0)
    # for l in lasts:
    #     print(l)
    return lasts[-1]

n = [3,20]
k = [5,2432902008176640000]
result = [
    [3,1,2],
    []
]

for q in [0,1]:
    qid = solution(n[q], k[q])
    if qid == result[q]:
        print(f'correct {qid}')
    else:
        print(f'incorrect {qid}')