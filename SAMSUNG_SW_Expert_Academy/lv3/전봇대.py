# 10580
# 연습문제

'''
2
3
1 10
5 5
7 7
2
1 1
2 2
'''
from itertools import combinations

testcase = int(input())
answer = []
for tc in range(testcase):
    number = int(input())
    lines = []
    total = 0
    for _ in range(number):
        lines.append(list(map(int, input().split())))
    
    for l1,l2 in combinations(lines, 2):
        if l1[0]-l2[0] >= 0 and l1[1]-l2[1] <= 0:
            total += 1
        elif l1[0]-l2[0] <= 0 and l1[1]-l2[1] >= 0:
            total += 1
    
    answer.append(f'#{tc+1} {total}')

for ans in answer:
    print(ans)