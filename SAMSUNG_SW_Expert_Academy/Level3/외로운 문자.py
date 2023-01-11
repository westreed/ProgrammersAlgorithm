# 10912
# 연습문제

'''
6
xxyyzz
yc
aaaab
bca
ppzqq
qnwerrewmq
'''

from collections import defaultdict

testcase = int(input())
answer = []
for tc in range(testcase):
    string = input().rstrip()
    count = defaultdict(int)
    result = []

    for s in string:
        count[s] += 1
    
    for s in count:
        if count[s] % 2 == 1:
            result.append(s)
    
    if result == []:
        answer.append(f'#{tc+1} Good')
    else:
        result.sort()
        answer.append(f'#{tc+1} {"".join(result)}')

for ans in answer:
    print(ans)