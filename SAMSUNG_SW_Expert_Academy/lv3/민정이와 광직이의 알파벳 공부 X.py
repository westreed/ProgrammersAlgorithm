# 9480
# 연습문제

# 입력
'''
2
10
cozy
lummox
gives
smart
squid
who
asks
for
job
pen
6
abcdefghi
jklmnopqr
stuvwxyz
zyxwvuts
rqponmlkj
ihgfedcba
'''

tc = int(input())
ans = ""

for t in range(tc):
    Number = int(input())
    WordList = [list(map(lambda x:ord(x)-96, list(input().strip()))) for _ in range(Number)]
    
    from copy import deepcopy
    from collections import deque
    queue = deque()
    for i in range(Number):
        queue.append([1, [True if i == j else False for j in range(Number)], WordList[i], sum(set(WordList[i]))])
    
    answer = []
    while queue:
        cnt, visit, word, sumw = queue.pop()
        if sumw == 351:
            answer.append(word)
            continue
        
        if cnt == len(WordList): continue

        for sel in range(cnt, Number):
            if visit[sel] is False:
                _word = word + WordList[sel]
                _visit = deepcopy(visit)
                _visit[sel] = True
                _sumw = sum(set(_word))
                queue.append([cnt+1, _visit, _word, _sumw])
    
    print(len(answer), answer)
