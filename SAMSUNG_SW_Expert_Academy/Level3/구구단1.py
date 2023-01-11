# 12004
# 연습문제

# 입력
'''
4
10
11
50
81
'''
from math import sqrt

case = int(input())
for c in range(case):
    number = int(input())
    result = []
    check  = False
    for i in range(1,int(sqrt(number))+1):
        a, b = divmod(number, i)
        if b == 0 and a < 10 and i < 10:
            check = True
            break
    
    if check is True: print(f'#{c+1} Yes')
    else: print(f'#{c+1} No')
