# 1926
# 연습문제

# 입력
'''
10
'''

num = int(input())
for n in range(1, num+1):
    n = str(n)
    c = sum([n.count('3'), n.count('6'), n.count('9')])
    if c == 0: print(n, end='')
    else:      print('-'*c, end='')
    print(' ', end='')