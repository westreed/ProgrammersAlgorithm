# 5293
# 연습문제

# 입력
'''
6
2 2 2 1
0 1 0 0
1 0 0 1
1 1 1 1
2 1 1 2
1 2 3 4
'''

from copy import deepcopy
from collections import deque

case = int(input())
answer = []
string = ['00', '01', '10', '11']
for c in range(case):
    Restore = list(map(int, input().split()))
    Length  = sum(Restore)
    Result  = ''

    queue = deque()
    for i in range(4):
        if Restore[i] > 0:
            _Restore = deepcopy(Restore)
            _Restore[i] -= 1
            queue.append([string[i], _Restore, Length-1])
    
    while queue:
        st, re, le = queue.popleft()

        if le == 0:
            Result = st
            break
        
        l_st = st[-1]
        for i in range(4):
            if re[i] > 0 and string[i][0] == l_st:
                _re = deepcopy(re)
                _re[i] -= 1
                queue.append([st+string[i][1], _re, le-1])

    if Result != '': answer.append(f'#{c+1} {Result}')
    else: answer.append(f'#{c+1} impossible')
    
for ans in answer:
    print(ans)