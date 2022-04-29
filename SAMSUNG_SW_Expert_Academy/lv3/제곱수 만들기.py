# 10965
# 연습문제

# 입력
'''
8
1
2
3
4
5
6
60
1000
'''
from collections import defaultdict

def factor(x):
    d = 2
    lists = defaultdict(int)
    cnt = 0
    while d <= x:
        cnt += 1
        if x % d == 0:
            lists[d] += 1
            x = x // d
        else:
            d += 1
    
    print(f'cnt : {cnt}\nlists : {lists}')
    return lists

answer = ''
for c in range(int(input())):
    answer += f'#{c+1} '
    number = int(input())

    lists = factor(number)
    value = 1
    for k, v in lists.items():
        if v % 2 != 0: value *= k
    
    answer += f'{value}\n'

print(answer)